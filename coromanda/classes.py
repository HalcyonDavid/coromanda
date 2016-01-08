
import numpy as np
import matplotlib.pyplot as plt
import yaml

import database as db

STAT = {'w5': db.w5}
COMP = {'w5': 'difference'}

def docomparison(a, b, ctype):
    if ctype == 'difference':
        return a - b
    if ctype == 'ratio':
        return a/b

class StatPlot(object):
    def __init__(self, stat, ids, outfile='txt.yaml'):
        self.stat = stat
        self.ids = ids
        self.outfile = outfile

    def loop(self):
        statdict = {}
        means = []
        stds = []
        for i in self.ids:
            a = STAT[self.stat](i)
            b = STAT[self.stat](i, home=False)
            comp = docomparison(a, b, COMP[self.stat])
            wl = db.win(i)
            try:
                statdict[comp].append(wl)
            except:
                statdict[comp] = [wl]
        for key in statdict:
            a = np.array(statdict[key])
            mean = np.mean(a)
            std = np.std(a)
            means.append((key, mean))
            stds.append((key, std))
        self.means = means
        self.stds = stds
        return self.means, self.stds

    def fit(self, data):
        data = np.array(data)
        x = data[:,0]
        y = data[:,1]
        z = np.polyfit(x, y, 2)
        return z

    def writer(self):
        printer = {self.stat: {'mean': self.meanfunc.tolist(),
                               'std': self.stdfunc.tolist()}
                   }
        with open (self.outfile, 'a') as f:
            f.write(yaml.dump(printer, default_flow_style=False))

    def saveplot():
        fig, (axl, axm, axr) = plt.subplots(3, 1)
        x = self.means[:,0]
        y = self.means[:1]
        func = np.poly1d(self.meanfunc)
        xnew = np.linspace(x.min, x.max, 50)
        ynew = func(xnew)
        axl.plot(x,y,'o', xnew, ynew)
        axl.title(self.stat + '_mean')
        x2 = self.stds[:,0]
        y2 = self.stds[:1]
        func2 = np.poly1d(self.stdfunc)
        ynew2 = func2(xnew)
        axm.plot(x,y2,'o', xnew, ynew2)
        axm.title(self.stat + '_std')
        axr.fill_between(x, (ynew + ynew2), (ynew - ynew2),
                         color='k', alpha=0.3)
        axr.plot(xnew, ynew)
        plt.tight_layout()
        plt.savefig(self.stat + '.pdf')

    def execute():
        mean, std = self.loop()
        self.meanfunc = self.fit(mean)
        self.stdfunc = self.fit(std)
        self.writer(self.outfile)
        self.saveplot()

class Calculate(object):
    def __init__(self, gid, sfile='txt.yaml', ofile='out.yaml'):
        self.gid = gid
        self.h = db.getname(gid)
        self.a = db.getname(gid, home=False)
        self.date = db.getdate(gid)
        self.sfile = sfile
        self.ofile = ofile

    def game(self, inputf=self.sfile):
        with open(inputf, 'r') as f:
            stats = yaml.load(f)
        means = []
        stds = []
        for s in stats:
            zmean = s['mean']
            zstd = s['std']
            fmean = np.poly1d(np.array(zmean))
            fstd = np.poly1d(np.array(zstd))

            a = STAT[s](self.gid)
            b = STAT[s](self.gid, home=False)
            comp = docomparison(a, b, COMP[s])
            means.append(float(fmean(comp)))
            stds.append(float(fstd(comp)))

        means = np.array(means)
        stds = np.array(stds)
        weighted = means * (1 / stds)
        bigsum = np.sum(weighted)

        stdsum = np.sum(1 / stds)
        self.res = float(bigsum / stdsum)
        return res

    def compare(self, ofile=self.ofile):
        hodddict = db.getodds(self.gid)
        aodddict = db.getodds(self.gid, home=False)
        hname = max(hodddict, key=hodddict.get)
        aname = max(aodddict, key=aodddict.get)
        hnum = hodddict[hname]
        anum = aodddict[aname]
        self.houtput = hnum * self.res
        self.aoutput = anum * self.res
        if self.houtput > 1 or self.aoutput > 1:
            self.good = True
        else:
            self.good = False
        printer = {self.h: {'web': hname,
                            'out': self.houtput},
                   self.a: {'web': aname,
                            'out': self.aoutput}
                   }
        with open(ofile, 'a') as f:
            f.write('\n-----------------\n\n')
            if self.good:
                f.write('****')
            f.write(self.date)
            f.write(self.gid + '\n')
            f.write(yaml.dump(printer, default_flow_style=False))
        return printer
