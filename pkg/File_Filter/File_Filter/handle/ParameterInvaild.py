import os
import logging 

import conf.conf as conf


#ParameterInvaild
#path: 文件路径
#fstr: 匹配的关键词集合
def ParameterInvaild(FilePaths , KeyWords ):
    logging.info("3.尝试进行参数检验")
        
    #尝试验证该路径是否能够正常打开和读取内容
    for path in FilePaths:
        flag1 = os.path.exists(path)
        if flag1 == False:
            WrongInfo = ("3.参数校验不合法： 这个文件不存在 {}".format(path))
            raise conf.Customization_Error(WrongInfo)
        flag2 = os.access(path,os.W_OK|os.R_OK)
        if flag2 == False: 
            WrongInfo = ("3.参数校验不合法： 我们无法打开这个文件路径 {}".format(path) )
            raise conf.Customization_Error(WrongInfo)
        
    #验证KeyWords是否非空
    if len(KeyWords) == 0:
        WrongInfo =("3.参数校验不合法： KeyWords为空 {}".format(KeyWords))
        raise conf.Customization_Error(WrongInfo) 
        
    logging.info("3.参数检验通过")
    #一切正常
    pass
