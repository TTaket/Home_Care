import logging
import os
import conf

#输入文件路径
def FileInit_Mode1():
    logging.info("FileMode 为 交互输入")
    Files = []
    while True:
        Path = input("请键入识别文件的相对路径或者绝对路径 以In文件夹为根目录/exit为停止:")
        if Path == '/exit':
            break
        else:
            Files.append(os.path.abspath(Path))
    print ("用户最后选择的路径为:{}".format(Files))
    logging.info("用户选择的路径为:{}".format(Files))
    return Files


#读入文件路径
def FileInit_Mode2():
    logging.info("FileMode 为 读入文件")
    Files = []
    print (conf.FILEPATH)
    f = open(conf.FILEPATH,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for path in flist:
        if len(path) == 0 or path[0] == '#':
            continue;
        Files.append(path)
    print ("用户最后选择的路径为:{}".format(Files))
    logging.info("用户选择的路径为:{}".format(Files))
    return Files