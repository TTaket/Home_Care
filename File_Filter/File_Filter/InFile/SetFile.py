import conf
import os
import logging
import shutil

def SetFile(FilePath):
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
    

    # 获取文件所在目录和完整文件名
    _, full_file_name = os.path.split(FilePath)
    file_name, file_ext = os.path.splitext(full_file_name)
    
    #可以正常读写
    source = FilePath
    target = conf.FILESPATH +file_name + file_ext
    logging.info("导入后文件路径为{}".format(target))

    shutil.copyfile(source, target)
    f = open(conf.FILEPATH , 'a' , encoding= 'utf-8')
    f.writelines(target+'\n')
    f.close()

    print ("File {} 导入成功".format(target))    
    logging.info("File {} 导入成功".format(target))
