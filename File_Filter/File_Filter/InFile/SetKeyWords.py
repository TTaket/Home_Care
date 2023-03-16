import conf
import os
import logging
import shutil

def SetKeyWords(FilePath):
    #改变工作路径
    os.chdir(conf.BASEPATH)
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
    target = conf.KEYWORDPATH

    shutil.copyfile(source, target)
    print ("KeyWords导入成功")    
    logging.info("KeyWords导入成功")
