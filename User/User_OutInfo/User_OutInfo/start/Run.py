# coding=utf-8    
import os
import logging 
import  conf.conf as conf

#修改位置
import  User.User_OutInfo.User_OutInfo.handle as handle

#主体运行程序
def ChooseWords(Info):
    #首先进行参数校验
    try:
        handle.ParameterInvaild(Info)
    except conf.Customization_Error as err:
        print (err.info)
        exit()
    else:
        pass

    handle.OutInfo(Info)