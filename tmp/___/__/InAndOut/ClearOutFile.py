import os
import conf.conf as conf
import logging

def ClearOutFile():

    #删除输出缓存文件
    if os.path.exists(conf.xx) == True:
        os.remove(conf.xx)
        logging.info("删除{}".format(conf.xx))
