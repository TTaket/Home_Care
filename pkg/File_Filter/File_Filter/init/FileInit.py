import logging
import  conf.conf as conf


#读入文件路径
def FileInit():
    Files = []
    f = open(conf.FF_FILELIST,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for path in flist:
        if len(path) == 0 or path[0] == '#':
            continue;
        Files.append(path)
    logging.info(f"2.初始化的文件为{Files}")
    return Files