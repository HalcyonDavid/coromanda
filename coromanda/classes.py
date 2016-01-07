import numpy as np
import matplotlib.pyplot as plt
import yaml

import database as db

STAT = {'w5': db.w5}

class StatPlot(object):
    def __init__(self, stat, ids, outfile='txt.yaml'):
        self.stat = stat
        self.ids = ids
        self.outfile = outfile

    def loop(self):
        statdict = {}
        means = []
        stds = []
        for i in self.ids
            a = STAT[self.stat](i)
            b = STAT[self.stat](i, home=False)
            diff = a - b
            wl = db.win(i)
            try:
                statdict[diff].append(wl)
            else
                statdict[diff] = [wl]
        for key in statdict:
            a = np.array(statdict[key])
            mean = np.mean(a)
            std = np.std(a)
            means.append((key, mean))
            stds.append((key, std))
        self.means = means
        self.stds = stds


    def fit(self, data):
        data = np.array(data)
        x = data[:0]
        y = data[:1]
        z = np.polyfit(x, y, 2)
        return z

    def writer(self):
        printer = {self.stat: {'mean': self.meanfunc.tolist(),
                               'std': self.stdfunc.tolist()}
                   }
        with open (self.outfile, 'a') as f:
            f.write(yaml.dump(printer, default_flow_style=False))

    def saveplot():
        x = self.means[:,0]
        y = self.means[:1]
        func = np.poly1d(self.meanfunc)
        xnew = np.linspace(x.min, x.max, 50)
        ynew = func(xnew)

        plt.plot(x,y,'o', xnew, ynew)
        plt.savefig(self.stat + '.pdf')

    def execute()
        mean, std = self.loop()
        self.meanfunc = self.fit(mean)
        self.stdfunc = self.fit(std)
        self.writer('txt.yaml')
        self.saveplot()

class Calculate(object):

    def __init__(self, gid):
        self.gid = gid
        self.h = db.gett(gid)
        self.a = db.gett(gid, home=False)
        self.date = db.getdate(gid)

    def game(self, gameid, inputf='txt.yaml'):
        with open(inputf, 'r') as f:
            stats = yaml.load(f)
        means = np.arry()
        stds = np.array()
        for s in stats:
            zmean = s['mean']
            zstd = s['std']
            fmean = np.poly1d(np.array(zmean))
            fstd = np.poly1d(np.array(zstd))

            a = STAT[s](gameid)
            b = STAT[s](gameid, home=False)
            diff = a-b
            means.append(fmean(diff))
            stds.append(fstd(diff))

        weighted = means * (1 / stds)
        bigsum = np.sum(weighted)

        stdsum = np.sum(1 / stds)
        self.res = float(weighted / stdsum)
        return res

    def compare(self, ofile='out.yaml'):
        hodddict = db.getodd(self.gid)
        aodddict = db.getodd(self.gid, home=False)
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
            f.write(yaml.dump(printer, default_flow_style=False)
        return printer
