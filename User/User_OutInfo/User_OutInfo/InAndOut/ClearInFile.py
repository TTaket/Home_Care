import os
import conf.conf as conf
import logging

#清除输入缓冲区
def ClearInFile():

    if os.path.exists(conf.USEROUTINFO_INFILE) == True:
        os.remove(conf.USEROUTINFO_INFILE)
        logging.info(f"5.删除{conf.USEROUTINFO_INFILE}")


