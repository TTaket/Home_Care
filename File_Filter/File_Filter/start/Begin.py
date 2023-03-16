#!/usr/bin/python
# coding=utf-8    
import os
import sys
import logging 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import conf
import init
import Run

#程序运行入口
#返回是否找到对应的关键词
def Begin():
    print ("程序开始运行")
    logging.info("程序开始运行")
    #改变工作路径
    os.chdir(conf.INPATH)

    #Find_Flag 表示是否找到对应的关键词
    Find_Flag = False

    #logging 的初始化
    init.Log()
    logging.info("logging开始运行...")

    #文件的初始化
    #Files = init.File_Mode1()
    Files = init.File_Mode2()
    logging.info("File开始运行...")

    #关键词的初始化
    #words = init.KeyWord_Mode1()
    words = init.KeyWord_Mode2()
    logging.info("KeyWord开始运行...")
        
    #启动程序
    Find_Flag = Run.Run(Files , words)

    print ("程序运行结束")
    logging.info("程序开始结束")
    return Find_Flag
