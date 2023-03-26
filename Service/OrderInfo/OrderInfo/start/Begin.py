import logging 
import  conf.conf as conf


#修改位置
import  Service.OrderInfo.OrderInfo.init as init



#程序初始化
def Begin():
    #用户信息初始化
    User = init.User()
    #需求信息初始化
    Demand = init.Demand()
    #关键词信息初始化
    KeyWord = init.KeyWord()
    return User , Demand , KeyWord
