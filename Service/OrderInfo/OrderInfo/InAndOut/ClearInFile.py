import os
import conf.conf as conf
import logging

def ClearInFile():

    if os.path.exists(conf.ORDERINFO_INFILE) == True:
        os.remove(conf.ORDERINFO_INFILE)
        logging.info("8.删除{}".format(conf.ORDERINFO_INFILE))


