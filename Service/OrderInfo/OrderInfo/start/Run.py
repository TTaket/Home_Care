# coding=utf-8    
import os
import logging 
import  conf.conf as conf
import  Service.OrderInfo.OrderInfo.handle as handle

#主体运行程序
def Run(User , Demand , KeyWord ,url):
    #首先进行参数校验
    try:
        handle.ParameterInvaild(User , Demand , KeyWord)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit
    else:
        logging.info("参数校验通过")
 
    try:
        OrderInfo = handle.OrderGen(KeyWord[0] ,User , Demand)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit
    else:
        print ("订单号生成成功")
        logging.info("订单号生成成功")
       
    logging.info("即将发送的数据信息: {}".format(OrderInfo))
    
    #发送订单
    ret = handle.OrderSend(OrderInfo , url)

    return ret
