function [ value ] = getinfo(info, ID)
    % info = home,away,winner,gameType
    c = database('halcyonnhl','root','password','com.mysql.jdbc.Driver','jdbc:mysql://localhost:3306/halcyonnhl');
    % Set format for DB output
    setdbprefs('DataReturnFormat','cellarray');
    q = sprintf('SELECT COUNT(*) FROM games WHERE winner=''%s'' and gameID<%d and gameID>%d',team,ID,ID-2000);
	q = sprintf('SELECT %s FROM games WHERE gameID=%d',info,ID)
    cu = exec(c,q);
    cu = fetch(cu);
    temp = cu.data;
	value = mat2str(cell2mat(temp))
end

function [ value ] = getstat(stat, team, ID)
    c = database('halcyonnhl','root','password','com.mysql.jdbc.Driver','jdbc:mysql://localhost:3306/halcyonnhl');
    % Set format for DB output
    setdbprefs('DataReturnFormat','cellarray');
    elseif strcmp(stat,'W5')
        q = sprintf('SELECT COUNT(*) FROM (SELECT * from altgames WHERE team=''%s'' AND gameID < %d ORDER BY gameID DESC LIMIT 5) AS S WHERE result=''%s''',team,ID,'W');
        cu = exec(c,q);
        cu = fetch(cu);
        temp = cell2mat(cu.data);
        value = mat2str(temp)
end
