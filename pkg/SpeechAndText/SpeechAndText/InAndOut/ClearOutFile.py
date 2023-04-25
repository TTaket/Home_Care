import os
import  conf.conf as conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.SAT_ANSFILE) == True:
        os.remove(conf.SAT_ANSFILE)
        logging.info("删除{}".format(conf.SAT_ANSFILE))
