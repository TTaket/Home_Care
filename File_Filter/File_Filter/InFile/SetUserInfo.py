import conf
import os
import logging
import shutil

def SetUserInfo(FilePath):

    #尝试验证该路径是否能够正常打开和读取内容
    FilePath = os.path.abspath(FilePath)
    flag1 = os.path.exists(FilePath)
    if flag1 == False:
        raise conf.Customization_Error("参数校验不合法： 这个文件不存在 {}".format(FilePath))
    flag2 = os.access(FilePath,os.R_OK)
    if flag2 == False: 
        raise conf.Customization_Error("参数校验不合法： 我们无法打开这个文件路径 {}".format(FilePath) )
    
    #可以正常读写
    source = FilePath
    target = conf.USERINFOPATH

    shutil.copyfile(source, target)
    print ("{}导入成功".format(target))    
    logging.info("{}导入成功".format(target))
