#!/usr/bin/python
# coding=utf-8    
import os
import conf
import sys
import logging 
#sys.path.append(r'../init/')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import init
import start.Run as Run

#程序运行入口
def Begin():
    print ("程序开始运行")
    logging.info("程序开始运行")
    #改变工作路径
    os.chdir(conf.INPATH)

    #Find_Flag 表示是否找到对应的关键词
    Find_Flag = False

    while (not Find_Flag):
        #logging 的初始化
        init.Log()
        logging.info("logging开始运行...")

        #调用语音识别API 生成文件保存到Files


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
