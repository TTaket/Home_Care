import  conf.conf as conf
import os
import logging
import shutil

#xx_INPATH 改成对应的
def SetFile(Path):
    #尝试验证该路径是否能够正常打开和读取内容
    Path = os.path.abspath(Path)
    flag1 = os.path.exists(Path)
    if flag1 == False:
        raise conf.Customization_Error(f"参数校验不合法： 这个文件不存在 {Path}")
    flag2 = os.access(Path,os.R_OK)
    if flag2 == False: 
        raise conf.Customization_Error(f"参数校验不合法： 我们无法打开这个文件路径 {Path}")
    
    #可以正常读写
    source = Path
    target = conf.USERINTERACT_INFILE
    logging.info("导入后文件路径为{}".format(target))
    shutil.copyfile(source, target)

    logging.info("File {} 导入成功".format(target))
