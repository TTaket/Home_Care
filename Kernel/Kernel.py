import conf.conf as conf
import Service as Service
import User as User
import pkg as pkg
import Kernel.ClearTmp as ClearTmp
import logging
import os

def Start_Work():
    #取消标记
    while True:
        #1.进行语音输入 把文件发送到ff的缓冲区里面
        logging.info("Kernel:进入语音读入模块")
        #语音读入和用户输入模块还没写先跳过第一步骤

        
        #2.把关键字进行提取发送到会Kernel里面
        logging.info("Kernel:进入关键词读取模块")
        f = open(conf.KERNELTMPFILELIST , 'r' ,encoding="utf-8")
        flist =  f.read().splitlines()
        fflist = []
        for File in flist:
            if len(File) == 0 or File[0]=='#':
                continue
            fflist.append(os.path.abspath(File))
            
        pkg.FFDeal(fflist , conf.KERNELTMPPATH)

        
        #3.交互确定是否是这个需求 
        logging.info("Kernel:进入交互确定模块")
        User.ChooseWords(conf.KERNELTMPPATH+conf.TMPFILE , conf.KERNELTMPPATH)
        
        #打开文件把关键词读取出来
        f = open(conf.KERNELTMPPATH+conf.TMPFILE , 'r' ,encoding="utf-8")
        words =  f.read().splitlines()
        retword = []
        for word in words:
            #空行和注释内容跳过
            if len(word) == 0 or word[0]=='#':
                continue

            #sys特殊处理
            if len(word)>=3 and word[0:3] == "sys": #特殊选项
                if word == "sys:强制退出":
                    logging.info("Kernel:用户自行选择退出")
                    print("Kernel:用户自行选择退出")
                    exit()
                else:
                    continue
            #常规内容
            retword.append(word) 
        #如果关键词为空 则返回
        if retword != []:
            break
        else:
            print("Kernel:本轮并没有识别出您的需求 请您重新说一次")
            logging.info("Kernel:本轮并没有识别出您的需求 请您重新说一次")
        
    #4.根据识别的内容执行不同的函数 分为订单打印 音乐 等等
    logging.info("Kernel:进入分发过程模块")
    if retword[0] in conf.Orderlist:
        logging.info("Kernel:进入订单模块")
        Service.Order(conf.KERNELTMPPATH+conf.TMPFILE , conf.KERNELTMPPATH)
    elif retword[0] in conf.locallist:
        logging.info("Kernel:进入本地模块")
        pass
    else:
        logging.error("Kernel:分发器错误")
        pass

    #5. 对用户进行输出
    logging.info("Kernel:进入输出模块")
    User.OutInfo(conf.KERNELTMPPATH+conf.TMPFILE)

    #6. 结束运行
    #ClearTmp.ClearOutFile()
    exit()


