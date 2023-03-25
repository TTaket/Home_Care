import os
import Home_care.conf.conf as conf
import logging

def ClearInFile():

    if os.path.exists(conf.USERINTERACT_INPATH) == True:
        os.remove(conf.USERINTERACT_INPATH)
        logging.info("删除{}".format(conf.USERINTERACT_INPATH))


