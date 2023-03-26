import os
import conf.conf as conf
import logging

def ClearInFile():

    if os.path.exists(conf.USERINTERACT_INFILE) == True:
        os.remove(conf.USERINTERACT_INFILE)
        logging.info("7.删除{}".format(conf.USERINTERACT_INFILE))


