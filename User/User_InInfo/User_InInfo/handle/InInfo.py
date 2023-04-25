import logging 
import pkg as pkg
import conf.conf as conf

#把内容打印到用户终端
def User_InInfo():
    #调用语音识别读入信息 把文件读入输入缓冲区
    pkg.StoT(conf.USERININFO_INPATH)
    
    
    