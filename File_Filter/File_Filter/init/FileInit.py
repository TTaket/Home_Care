import logging
import os


#输入文件路径
def FileInit_Mode1():
    logging.info("FileMode 为 交互输入")
    Files = []
    while True:
        Path = input("请键入识别文件的相对路径或者绝对路径/exit为停止:")
        if Path == '/exit':
            break
        else:
            Files.append(os.path.abspath(Path))
    print ("用户最后选择的路径为:{}".format(Files))
    logging.info("用户选择的路径为:{}".format(Files))
    return Files


#读入文件路径
def FileInit_Mode2():
    pass