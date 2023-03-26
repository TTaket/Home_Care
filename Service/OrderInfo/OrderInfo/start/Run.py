# coding=utf-8    
import os
import logging 
import  conf.conf as conf
import  Service.OrderInfo.OrderInfo.handle as handle

#主体运行程序
def Run(User , Demand , KeyWord):
    #首先进行参数校验
    try:
        handle.ParameterInvaild(User , Demand , KeyWord)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit()
    else:
        pass
 
    #创建并且打开一个存储答案的文档
    fans = open(conf.ORDERINFO_OUTFILE,'w',encoding='utf-8') 

    try:
        OrderInfo = handle.OrderGen(KeyWord[0] ,User , Demand)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit()
    else:
        pass
    
    #发送订单
    ret = handle.OrderSend(OrderInfo)
    
    fans.writelines(ret +'\n')
    #关闭所有的文件
    fans.close()
    logging.info("6.关闭导出文件文件")
