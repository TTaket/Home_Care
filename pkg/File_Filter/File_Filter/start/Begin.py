
import logging 
import  conf.conf as conf
import  pkg.File_Filter.File_Filter.init as init



#程序运行入口
#可支持开启时设置运行模式 默认文档读入
#返回是否找到对应的关键词
def Begin():
    Keywords = init.KeyWord()
    Files = init.File()

    return Files , Keywords
