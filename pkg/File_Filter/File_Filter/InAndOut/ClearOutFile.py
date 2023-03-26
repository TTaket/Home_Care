import os
import conf.conf as conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.FF_ANSFILE) == True:
        os.remove(conf.FF_ANSFILE)
        logging.info("7.删除{}".format(conf.FF_ANSFILE))
