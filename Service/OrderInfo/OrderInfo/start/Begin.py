import logging 
import Home_care.conf.conf as conf


#修改位置
import Home_care.Service.OrderInfo.OrderInfo.init as init



#程序初始化
def Begin():
    print ("Begin初始配置开始")
    #初始化
    User = init.User()
    print ("User初始化结果{}".format(User))
    logging.info("User初始化结果{}".format(User))
    
    Demand = init.Demand()
    print ("Demand初始化结果{}".format(Demand))
    logging.info("Demand初始化结果{}".format(Demand))
    
    KeyWord = init.KeyWord()
    print ("Demand初始化结果{}".format(Demand))
    logging.info("Demand初始化结果{}".format(Demand))

    return User , Demand , KeyWord
