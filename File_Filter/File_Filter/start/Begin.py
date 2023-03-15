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
    init.LogInit()
    logging.info("logging开始运行...")

    #输入文件路径
    Files = []
    while True:
        Path = input("请键入识别文件的相对路径或者绝对路径/exit为停止:")
        if Path == '/exit':
            break
        else:
            Files.append(os.path.abspath(Path))
    print ("用户最后选择的路径为:{}".format(Files))
    logging.info("用户选择的路径为:{}".format(Files))

    #输入关键词
    words = []
    while True:
        word = input("请输入关键词并/exit为停止:")
        if word == '/exit':
            break
        else:
            words.append(word)
    print ("用户最后选择的关键词为:{}".format(words))
    logging.info("用户最后选择的关键词为:{}".format(words))
    
    #启动程序
    print ("程序开始运行")
    logging.info("程序开始运行")
    Run.Run(Files , words)
    print ("程序运行结束")
    logging.info("程序开始结束")

Begin()