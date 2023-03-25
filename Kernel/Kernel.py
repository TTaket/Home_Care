import Home_care.conf.conf as conf
import Home_care.Service as Service
import Home_care.User as User
import Home_care.pkg as pkg
import logging

def Deal():
    while True:
        #1.进行语音输入 把文件发送到ff的缓冲区里面
        #语音读入和用户模块还没写先跳过第一步骤

        #2.把关键字进行提取发送到会Kernel里面
        pkg.FFDeal(conf.FF_INPATH , conf.KERNELTMPPATH)

        #3.交互确定是否是这个需求 
        retword = User.User_ChooseWords(conf.KERNELTMPPATH , conf.KERNELTMPPATH)
        #如果关键词为空 则返回
        if len(retword) != 0:
            break;
        else:
            print("本轮并没有识别出您的需求 请您重新说一次")
            logging.info("本轮并没有识别出您的需求 请您重新说一次")
    
    #4.根据识别的内容执行不同的函数 分为订单打印 音乐 等等
    if retword[0] in conf.Orderlist:
        Service.OrderGenandSend(conf.KERNELTMPPATH , conf.TESTURL)
    elif retword[0] in conf.locallist:
        pass

    #5. 结束
