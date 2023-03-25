import logging
import Home_care.conf.conf as conf


#读入文件路径
def FileInit():
    Files = []
    f = open(conf.USERINTERACT_INFILE,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for path in flist:
        if len(path) == 0 or path[0] == '#':
            continue;
        Files.append(path)
    return Files