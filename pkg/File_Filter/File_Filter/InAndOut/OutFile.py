import os
import conf.conf as conf
import logging
import shutil

#传入导出的位置
def OutFile(FilePath , Filename):
    FilePath = os.path.abspath(FilePath)

    logging.info(f"6.尝试把输出缓冲区信息导出到{FilePath}")
    #检查缓冲区答案文件是否存在
    flag1 = os.path.exists(conf.FF_ANSFILE)
    if flag1 == False:
        WrongInfo = ("6.无法在输出缓冲区找到需求信息")
        raise conf.Customization_Error(WrongInfo)
    
    logging.info("6.成功在输出缓冲区找到需求信息")
    #如果没有对应的生成位置的路径 如果没有则生成对应路径
    if os.path.exists(FilePath) == False:
        os.makedirs(FilePath)
    
    #可以正常读写
    source = conf.FF_ANSFILE
    target = FilePath +'/' +Filename
    logging.info(f"6.文件从{source}导出到{target}")
    shutil.copyfile(source, target)
    logging.info("6.导出成功")

