import time
import logging
import conf


#OrderGen
#传入关键词
#传出的是订单号 OrderID
def OrderGen(keyword , UserInfo , Demand_dic):
    #获取用户ID
    if UserInfo.get("ID") == None:
        raise conf.Customization_Error("UserInfo中找不到ID标签")
    if len(UserInfo["ID"])<6 :
        raise conf.Customization_Error("UserInfo中的ID 过短无法截取")
    UserID = UserInfo["ID"][-6:]
    logging.info("获取的用户ID 为{}".format(UserID))
    
    #获取需求ID
    if Demand_dic.get(keyword) == None:
        raise conf.Customization_Error("需求库中找不到对应需求 - {}".format(keyword))
    DemandID = Demand_dic[keyword]
    logging.info("获取的需求ID 为{}".format(DemandID))

    #获取时间
    DateTime = str("{}".format(time.strftime('%y%m%d%H%M%S',time.localtime())))
    logging.info("获取的时间 为{}".format(DateTime))

    #加密
    OrderID = DateTime+UserID+DemandID
    logging.info("生成的OrderID 为{}".format(OrderID))

    #生成对应订单
    return OrderID