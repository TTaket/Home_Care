import conf.conf as conf
import logging
import os
import shutil


#传入导出的位置
def OutFile(Path , Name):
    Path = os.path.abspath(Path)
    
    
    #检查缓冲区答案文件是否存在
    logging.info("6.即将检验缓冲区是否有需求信息")
    flag1 = os.path.exists(conf.USERINTERACT_OUTFILE)
    if flag1 == False:
        WrongInfo = "无法在输出缓冲区找到需求信息"
        logging.error(WrongInfo)
        raise conf.Customization_Error(WrongInfo)
    
    logging.info("6.成功在输出缓冲区找到需求信息")

    #如果没有对应的生成位置的路径 如果没有则生成对应路径
    if os.path.exists(Path) == False:
        os.makedirs(Path)
    
    #可以正常读写
    source = conf.USERINTERACT_OUTFILE
    target = Path +'/' +Name
    logging.info(f"6.即将尝试从{source}导出文件到{target}")
    shutil.copyfile(source, target)
    logging.info("6.导出成功")

    

