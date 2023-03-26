import os
import logging
import conf.conf as conf
import Kernel.Init as Init

#################################
#
#  这个文件里面的都是预先执行的配置文件
#
#################################

#改变工作路径到根目录
os.chdir(conf.BASEPATH)

#logging 的初始化
Init.Log()
print ("Kernel:logging运行")
logging.info("Kernel:logging开始运行...")