
import conf.conf as conf
import Service as Service
import User as User
import pkg as pkg
import logging
import os

def Deal():
    while True:
        #1.进行语音输入 把文件发送到ff的缓冲区里面
        #语音读入和用户模块还没写先跳过第一步骤

        #2.把关键字进行提取发送到会Kernel里面
        f = open(conf.KERNELTMPFILELIST , 'r' ,encoding="utf-8")
        flist =  f.read().splitlines()
        fflist = []
        for File in flist:
            if len(File) == 0 or File[0]=='#':
                continue
            fflist.append(os.path.abspath(File))
            
        pkg.FFDeal(fflist , conf.KERNELTMPPATH)

        #3.交互确定是否是这个需求 
        User.User_ChooseWords(conf.KERNELTMPPATH , conf.KERNELTMPPATH)
        
        #打开文件把关键词读取出来
        f = open(conf.KERNELTMPPATH+conf.TMPFILE , 'r' ,encoding="utf-8")
        words =  f.read().splitlines()
        retword = []
        for word in words:
            if len(word) == 0 or word[0]=='#':
                continue

            retword.append(word) 
        #如果关键词为空 则返回
        if retword != []:
            break
        else:
            print("本轮并没有识别出您的需求 请您重新说一次")
            logging.info("本轮并没有识别出您的需求 请您重新说一次")
    
    #4.根据识别的内容执行不同的函数 分为订单打印 音乐 等等
    if retword[0] in conf.Orderlist:
        Service.OrderGenandSend(conf.KERNELTMPPATH+conf.TMPFILE , conf.TESTURL)
    elif retword[0] in conf.locallist:
        pass
    
    #5. 结束
    exit()

Deal()


