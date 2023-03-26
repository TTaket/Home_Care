import os
import logging 

import conf.conf as conf


#ParameterInvaild
#path: 文件路径
#fstr: 匹配的关键词集合
def ParameterInvaild(UserInfo_dic , DemandInfo_dic , KeyWords):
    
    logging.info("3.即将进行参数匹配")
    #验证KeyWords是否非空
    if len(KeyWords) == 0:
        WrongInfo = ("3.参数校验不合法： KeyWords为空 {}".format(KeyWords))
        raise conf.Customization_Error(WrongInfo) 
    
    #验证UserInfo是否非空
    if len(UserInfo_dic) == 0:
        WrongInfo = ("3.参数校验不合法： UserInfo_dic为空 {}".format(UserInfo_dic))
        raise conf.Customization_Error(WrongInfo) 
    
    #验证DemandInfo是否非空
    if len(DemandInfo_dic) == 0:
        WrongInfo = ("3.参数校验不合法： DemandInfo_dic为空 {}".format(DemandInfo_dic))
        raise conf.Customization_Error(WrongInfo) 
        
    logging.info("3.参数匹配一切正常")
    #一切正常
    pass
