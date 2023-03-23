import os
import conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.ANSFILEPATH) == True:
        os.remove(conf.ANSFILEPATH)
        logging.info("删除{}".format(conf.ANSFILEPATH))
