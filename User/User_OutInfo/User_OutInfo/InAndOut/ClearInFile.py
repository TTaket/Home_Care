import os
import Home_care.conf.conf as conf
import logging

def ClearInFile():

    if os.path.exists(conf.xx_INPATH) == True:
        os.remove(conf.xx_INPATH)
        logging.info("删除{}".format(conf.xx_INPATH))


