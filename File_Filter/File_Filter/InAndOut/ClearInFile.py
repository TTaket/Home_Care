import os
import conf
import logging
import shutil

def ClearInFile():

    #删除需求文件
    if os.path.exists(conf.DEMANDINFOPATH) == True:
        os.remove(conf.DEMANDINFOPATH)
        logging.info("删除{}".format(conf.DEMANDINFOPATH))

    #删除关键词文件
    if os.path.exists(conf.KEYWORDPATH) == True:
        os.remove(conf.KEYWORDPATH)
        logging.info("删除{}".format(conf.KEYWORDPATH))

    #删除用户文件
    if os.path.exists(conf.USERINFOPATH) == True:
        os.remove(conf.USERINFOPATH)
        logging.info("删除{}".format(conf.USERINFOPATH))
    
    #删除文件目录
    if os.path.exists(conf.FILEPATH) == True:
        os.remove(conf.FILEPATH)
        logging.info("删除{}".format(conf.FILEPATH))

    #删除具体文件
    if os.path.exists(conf.FILESPATH) == True:
        shutil.rmtree(conf.FILESPATH) 
        logging.info("删除{}".format(conf.FILESPATH))
