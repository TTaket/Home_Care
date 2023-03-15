import os
import logging 


#Customization error
#Using: 
#    Customization_Error(problem)
class Customization_Error(RuntimeError):
    def __init__(self , arg):
        self.info = arg
    def __str__(self):
        return str(self.info)


#ParameterInvaild
#path: 文件路径
#fstr: 匹配的关键词集合
def ParameterInvaild(Allpath , fstr):
    logging.info("path: {} , fstr: {}".format(Allpath , fstr))
        
    #尝试验证该路径是否能够正常打开和读取内容
    for path in Allpath:
        flag1 = os.path.exists(path)
        if flag1 == False:
            raise Customization_Error("参数校验不合法： 这个文件不存在 {}".format(path))
        flag2 = os.access(path,os.W_OK|os.R_OK)
        if flag2 == False: 
            raise Customization_Error("参数校验不合法： 我们无法打开这个文件路径 {}".format(path) )
    #一切正常
    pass
