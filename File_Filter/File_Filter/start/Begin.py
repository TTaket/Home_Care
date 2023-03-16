#!/usr/bin/python
# coding=utf-8    
import os
import sys
import logging 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import conf
import init

#程序运行入口
#可支持开启时设置运行模式 默认文档读入
#返回是否找到对应的关键词
def Begin(FileMode=2 ,KeyWordMode =2):
    print ("程序开始运行")
    #改变工作路径
    os.chdir(conf.BASEPATH)

    Begin_dic = {}
    #logging 的初始化
    init.Log()
    logging.info("logging开始运行...")
    
    #文件的初始化
    if FileMode == 1:
        Files = init.File_Mode1()
    elif FileMode == 2:
        Files = init.File_Mode2()
    else:
        #TODO： 可用异常去升级
        print ("错误的文件模式")
        exit
    logging.info("File开始运行...")

    #关键词的初始化
    if KeyWordMode == 1:
        words = init.KeyWord_Mode1()
    elif KeyWordMode == 2:
        words = init.KeyWord_Mode2()
    else:
        #TODO： 可用异常去升级
        print ("错误的关键词模式")
        exit
    logging.info("KeyWord开始运行...")
        
    #用户信息初始化
    UserInfo_dic = init.UserInfo()

    #需求列表初始化
    DemandInfo_dic = init.DemandInfo()

    Begin_dic.update({"FilePaths":Files})
    Begin_dic.update({"KeyWords":words})
    Begin_dic.update({"UserInfo":UserInfo_dic})
    Begin_dic.update({"DemandInfo":DemandInfo_dic})

    print ("程序运行结束")
    return Begin_dic
