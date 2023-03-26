import os
import conf.conf as conf
import logging
import shutil

def ClearOutFile():

    #删除临时文件
    if os.path.exists(conf.KERNELTMPPATH+conf.TMPFILE) == True:
        os.remove(conf.KERNELTMPPATH+conf.TMPFILE)
        logging.info("Kernel:删除{}".format(conf.KERNELTMPPATH+conf.TMPFILE))

    #删除文件路径
    if os.path.exists(conf.KERNELTMPFILELIST) == True:
        os.remove(conf.KERNELTMPFILELIST)
        logging.info("Kernel:删除{}".format(conf.KERNELTMPFILELIST))
    
    #删除具体文件
    if os.path.exists(conf.KERNELTMPFILEPATH) == True:
        shutil.rmtree(conf.KERNELTMPFILEPATH)
        logging.info("Kernel:删除{}".format(conf.KERNELTMPFILEPATH))
    
