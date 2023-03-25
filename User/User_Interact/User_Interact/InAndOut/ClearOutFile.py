import os
import Home_care.conf.conf as conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.USERINTERACT_OUTPATH) == True:
        os.remove(conf.USERINTERACT_OUTPATH)
        logging.info("删除{}".format(conf.USERINTERACT_OUTPATH))
