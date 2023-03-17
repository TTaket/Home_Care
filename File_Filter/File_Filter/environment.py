import File_Filter.File_Filter.conf as conf
import File_Filter.File_Filter.init as init
import os
import sys
import logging

#################################
#
#  这个文件里面的都是预先执行的配置文件
#
#################################

#改变工作路径
os.chdir(conf.BASEPATH)

#logging 的初始化
init.Log()
print ("logging运行")
logging.info("logging开始运行...")