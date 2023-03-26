import  conf.conf as conf
import os
import logging
import shutil

#xx_INPATH 改成对应的
def SetFile(Path):
    #尝试验证该路径是否能够正常打开和读取内容
    Path = os.path.abspath(Path)
    logging.info(f"1.即将检验传入的文件是否可以打开:{Path}")

    #检测点1： 检测是否存在
    flag1 = os.path.exists(Path)
    if flag1 == False:
        WrongInfo = (f"1.参数校验不合法： 这个文件不存在 {Path}")
        logging.error(WrongInfo)
        raise conf.Customization_Error(WrongInfo)
    
    #检测点2： 检测是否可读
    flag2 = os.access(Path,os.R_OK)
    if flag2 == False: 
        WrongInfo = (f"1.参数校验不合法： 我们无法打开这个文件路径 {Path}")
        logging.error(WrongInfo)
        raise conf.Customization_Error(WrongInfo)
    
    logging.info("1.传入文件可以打开")
    
    #可以正常读写
    source = Path
    target = conf.USEROUTINFO_INFILE
    logging.info(f"1.导入后文件路径为{target}")
    shutil.copyfile(source, target)
    logging.info("1.导入成功")
