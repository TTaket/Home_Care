import os
import  conf.conf as conf
import logging

def ClearInFile():

    if os.path.exists(conf.xx_INFILE) == True:
        os.remove(conf.xx_INFILE)
        logging.info("删除{}".format(conf.xx_INFILE))


