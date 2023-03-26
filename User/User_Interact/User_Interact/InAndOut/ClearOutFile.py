import os
import conf.conf as conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.USERINTERACT_OUTFILE) == True:
        os.remove(conf.USERINTERACT_OUTFILE)
        logging.info("7.删除{}".format(conf.USERINTERACT_OUTFILE))
