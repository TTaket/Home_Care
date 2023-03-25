import os
import logging 

from conf import Customization_Error 


#ParameterInvaild
#path: 文件路径
#fstr: 匹配的关键词集合
def ParameterInvaild(UserInfo_dic , DemandInfo_dic , KeyWords):
    logging.info("User: {} , Demand: {} , KeyWords: {}".format(UserInfo_dic , DemandInfo_dic , KeyWords))
        
    
    #验证KeyWords是否非空
    if len(KeyWords) == 0:
        raise Customization_Error("参数校验不合法： KeyWords为空 {}".format(KeyWords)) 
    
    #验证UserInfo是否非空
    if len(UserInfo_dic) == 0:
        raise Customization_Error("参数校验不合法： UserInfo_dic为空 {}".format(UserInfo_dic)) 
    
    #验证DemandInfo是否非空
    if len(DemandInfo_dic) == 0:
        raise Customization_Error("参数校验不合法： DemandInfo_dic为空 {}".format(DemandInfo_dic)) 
        
    #一切正常
    pass
