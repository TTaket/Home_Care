import os
import  conf.conf as conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.USERININFO_ANSFILE) == True:
        os.remove(conf.USERININFO_ANSFILE)
        logging.info("删除{}".format(conf.USERININFO_ANSFILE))
