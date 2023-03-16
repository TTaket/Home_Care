import os
import logging 

from conf import Customization_Error 


#ParameterInvaild
#path: 文件路径
#fstr: 匹配的关键词集合
def ParameterInvaild(FilePaths , KeyWords , UserInfo_dic , DemandInfo_dic):
    logging.info("path: {} , KeyWords: {}".format(FilePaths , KeyWords))
    logging.info("UserInfo_dic: {} , DemandInfo_dic: {}".format(UserInfo_dic , DemandInfo_dic))
        
    #尝试验证该路径是否能够正常打开和读取内容
    for path in FilePaths:
        flag1 = os.path.exists(path)
        if flag1 == False:
            raise Customization_Error("参数校验不合法： 这个文件不存在 {}".format(path))
        flag2 = os.access(path,os.W_OK|os.R_OK)
        if flag2 == False: 
            raise Customization_Error("参数校验不合法： 我们无法打开这个文件路径 {}".format(path) )
    
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
