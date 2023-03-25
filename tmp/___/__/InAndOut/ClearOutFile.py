import os
import  conf.conf as conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.xx_OUTFILE) == True:
        os.remove(conf.xx_OUTFILE)
        logging.info("删除{}".format(conf.xx_OUTFILE))
