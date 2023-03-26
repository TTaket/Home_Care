import os
import conf.conf as conf
import logging
import shutil

#传入导出的位置
def OutFile(FilePath , Filename):
    FilePath = os.path.abspath(FilePath)
    
    #检查缓冲区答案文件是否存在
    flag1 = os.path.exists(conf.ORDERINFO_OUTFILE)
    if flag1 == False:
        print ("无法在输出缓冲区找到需求信息")
        logging.debug("无法在输出缓冲区找到需求信息")
        raise conf.Customization_Error("无法在输出缓冲区找到需求信息 {}".format(conf.FF_ANSFILE))
    
    logging.debug("成功在输出缓冲区找到需求信息")
    #如果没有对应的生成位置的路径 如果没有则生成对应路径
    if os.path.exists(FilePath) == False:
        os.makedirs(FilePath)
    
    
    #可以正常读写
    source = conf.ORDERINFO_OUTFILE
    target = FilePath +'/' +Filename
    logging.info("导出后文件路径为{}".format(target))
    print ("导出后文件路径为{}".format(target))

    shutil.copyfile(source, target)

