import os
import  conf.conf as conf
import logging

def ClearInFile():

    if os.path.exists(conf.USERININFO_INFILE) == True:
        os.remove(conf.USERININFO_INFILE)
        logging.info("删除{}".format(conf.USERININFO_INFILE))


