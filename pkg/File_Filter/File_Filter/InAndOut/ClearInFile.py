import os
import Home_care.conf.conf as conf
import logging
import shutil

def ClearInFile():

    #删除文件目录
    if os.path.exists(conf.FF_FILELIST) == True:
        os.remove(conf.FF_FILELIST)
        logging.info("删除{}".format(conf.FF_FILELIST))

    #删除具体文件
    if os.path.exists(conf.FF_FILEPATH) == True:
        shutil.rmtree(conf.FF_FILEPATH) 
        logging.info("删除{}".format(conf.FF_FILEPATH))
