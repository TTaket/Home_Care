#!/usr/bin/python
# coding=utf-8    
import os
import sys
import logging 
#sys.path.append(r'../init/')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import init
import Run

#程序运行入口
def Begin():
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
    print ("程序开始运行")
    logging.info("程序开始运行")
    Run.Run(Files , words)
    print ("程序运行结束")
    logging.info("程序开始结束")

Begin()