# coding=utf-8    
import os
import logging 
import  conf.conf as conf

import  User.User_InInfo.User_InInfo.handle as handle 

#主体运行程序
def Run():
    handle.InInfo()
    #解析文件内容
    finfo = open(conf.USERININFO_INFILE , 'r' ,encoding='utf-8')
    finfo_list = finfo.readlines()
    if len(finfo_list) == 0:
        raise conf.Customization_Error("未检测到语音输入")
    else:
        finfo_str = finfo_list[0]
    logging.info(f"读入的信息为：{finfo_str}")
    
    #转移到输出缓冲区
    os.system(f"cp {conf.USERININFO_INFILE} {conf.USERININFO_OUTPATH}")



    
