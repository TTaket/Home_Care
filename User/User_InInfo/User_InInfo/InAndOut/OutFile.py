import Home_care.conf.conf as conf
import logging
import os
import shutil


#xx_ANSFILE 改成对应名字
#传入导出的位置
def OutFile(Path , Name):
    Path = os.path.abspath(Path)
    
    #检查缓冲区答案文件是否存在
    flag1 = os.path.exists(conf.xx_ANSFILE)
    if flag1 == False:
        print ("无法在输出缓冲区找到需求信息")
        logging.debug("无法在输出缓冲区找到需求信息")
        raise conf.Customization_Error("无法在输出缓冲区找到需求信息 {}".format(conf.xx_ANSFILE))
    
    logging.debug("成功在输出缓冲区找到需求信息")
    #如果没有对应的生成位置的路径 如果没有则生成对应路径
    if os.path.exists(Path) == False:
        os.makedirs(Path)
    
    
    
    # 获取文件所在目录和完整文件名
    _, full_file_name = os.path.split(conf.xx_ANSFILE)
    file_name, file_ext = os.path.splitext(conf.xx_ANSFILE)
    
    #可以正常读写
    source = conf.xx_ANSFILE
    target = Path +'/' +Name
    logging.info("导出后文件路径为{}".format(target))
    print ("导出后文件路径为{}".format(target))

    shutil.copyfile(source, target)

