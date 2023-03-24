import os
import logging
import Home_care.conf.conf as conf
import Home_care.Kernel.Init as Init

#################################
#
#  这个文件里面的都是预先执行的配置文件
#
#################################

#改变工作路径到根目录
os.chdir(conf.BASEPATH)

#logging 的初始化
Init.Log()
print ("logging运行")
logging.info("logging开始运行...")