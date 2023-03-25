# coding=utf-8    
import os
import logging 
import Home_care.conf.conf as conf
import Home_care.pkg.yuyin_files as yuyin_files
import Home_care.User.User_InInfo.User_InInfo.handle as handle 

#主体运行程序
def Run():
    

    #创建并且打开一个存储答案的文档
    fans = open(conf.xx_ANSFILE,'w',encoding='utf-8')    
    
   
    
    #关闭所有的文件
    fans.close()
    logging.info("关闭文件")
    return True
