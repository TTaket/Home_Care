
import logging 
import  conf.conf as conf
import  pkg.File_Filter.File_Filter.init as init



#程序运行入口
#可支持开启时设置运行模式 默认文档读入
#返回是否找到对应的关键词
def Begin():
    print ("Begin初始配置开始")
    Keywords = init.KeyWord()
    Files = init.File()
    print ("File初始化结果{}".format(Files))
    logging.info("File初始化结果{}".format(Files))

    return Files , Keywords
