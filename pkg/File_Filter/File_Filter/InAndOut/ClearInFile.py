import os
import conf
import logging
import shutil

def ClearInFile():

    #删除文件目录
    if os.path.exists(conf.FILEPATH) == True:
        os.remove(conf.FILEPATH)
        logging.info("删除{}".format(conf.FILEPATH))

    #删除具体文件
    if os.path.exists(conf.FILESPATH) == True:
        shutil.rmtree(conf.FILESPATH) 
        logging.info("删除{}".format(conf.FILESPATH))
