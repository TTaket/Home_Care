import os
import conf
import logging

def UnInstall():
    
    #删除所有的导入文件
    f = open(conf.FILEPATH,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for path in flist:
        if len(path) == 0 or path[0] == '#':
            continue;
        os.remove(path)    
        logging.info("删除{}".format(path))
    f.close()
        
    #删除需求文件
    os.remove(conf.DEMANDINFOPATH)
    logging.info("删除{}".format(conf.DEMANDINFOPATH))

    #删除关键词文件
    os.remove(conf.KEYWORDPATH)
    logging.info("删除{}".format(conf.KEYWORDPATH))

    #删除用户文件
    os.remove(conf.USERINFOPATH)
    logging.info("删除{}".format(conf.USERINFOPATH))
    
    #删除文件目录
    os.remove(conf.FILEPATH)
    logging.info("删除{}".format(conf.FILEPATH))
