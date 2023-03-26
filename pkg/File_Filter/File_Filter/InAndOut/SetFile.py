import conf.conf as conf
import os
import logging
import shutil

def SetFile(FilePath):
    #尝试验证该路径是否能够正常打开和读取内容
    FilePath = os.path.abspath(FilePath)
    logging.info(f"1.进行文件读取测试{FilePath}")
    #第一个测试点：文件存在
    flag1 = os.path.exists(FilePath)
    if flag1 == False:
        WrongInfo = ("1.参数校验不合法： 这个文件不存在 {}".format(FilePath))
        raise conf.Customization_Error(WrongInfo)
    #第二个测试点：文件可读
    flag2 = os.access(FilePath,os.R_OK)
    if flag2 == False: 
        WrongInfo = ("1.参数校验不合法： 我们无法打开这个文件路径 {}".format(FilePath) )
        raise conf.Customization_Error(WrongInfo)
    logging.info(f"1.测试成功")
    
    #如果没有对应的Files文件夹 则生成一个
    if os.path.exists(conf.FF_FILEPATH) == False:
        os.mkdir(conf.FF_FILEPATH)

    # 获取文件所在目录和完整文件名
    _, full_file_name = os.path.split(FilePath)
    file_name, file_ext = os.path.splitext(full_file_name)
    
    #可以正常读写
    source = FilePath
    target = conf.FF_FILEPATH +file_name + file_ext
    logging.info("1.导入后文件路径为{}".format(target))

    shutil.copyfile(source, target)
    f = open(conf.FF_FILELIST , 'a' , encoding= 'utf-8')
    f.writelines(target+'\n')
    f.close()

    logging.info("1.导入成功")
