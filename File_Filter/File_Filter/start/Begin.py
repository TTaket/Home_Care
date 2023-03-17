#!/usr/bin/python
# coding=utf-8    
import os
import sys
import logging 


#增加包路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import conf
import init



#程序运行入口
#可支持开启时设置运行模式 默认文档读入
#返回是否找到对应的关键词
def Begin(FileMode=2 ,KeyWordMode =2):
    print ("Begin初始配置开始")
    
    #设置Begin包
    Begin_dic = conf.Begin_Info     

    #文件的初始化
    if FileMode == 1:
        Files = init.File_Mode1()
    elif FileMode == 2:
        Files = init.File_Mode2()
    else:
        #TODO： 可用异常去升级
        print ("错误的文件模式")
        exit
    print ("File初始化结果{}".format(Files))
    logging.info("File初始化结果{}".format(Files))

    #关键词的初始化
    if KeyWordMode == 1:
        words = init.KeyWord_Mode1()
    elif KeyWordMode == 2:
        words = init.KeyWord_Mode2()
    else:
        #TODO： 可用异常去升级
        print ("错误的关键词模式")
        exit
    print ("KeyWord初始化结果{}".format(words))
    logging.info("KeyWord初始化结果{}".format(words))
        
    #用户信息初始化
    UserInfo_dic = init.UserInfo()
    print ("UserInfo初始化结果{}".format(UserInfo_dic))
    logging.info("UserInfo初始化结果{}".format(UserInfo_dic))

    #需求列表初始化
    DemandInfo_dic = init.DemandInfo()
    print ("DemandInfo初始化结果{}".format(DemandInfo_dic))
    logging.info("DemandInfo初始化结果{}".format(DemandInfo_dic))

    #合并返回包
    Begin_dic.FilePaths = Files
    Begin_dic.KeyWords = words
    Begin_dic.UserInfo = UserInfo_dic
    Begin_dic.DemandInfo = DemandInfo_dic

    print ("Begin初始配置结束")
    return Begin_dic
