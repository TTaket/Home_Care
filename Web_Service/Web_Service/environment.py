import Web_Service.Web_Service.conf as conf
import Web_Service.Web_Service.init as init
import os
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