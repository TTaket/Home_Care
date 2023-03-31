import logging
import conf.conf as conf
import sys

def Check( typ , info):
    
    
    #info不为空
    if sys.getsizeof(info) == 0: 
        WrongInfo = (f"网络接口:发送信息不能为空 当前Info大小为{sys.getsizeof(info)}字节")
        raise conf.Customization_Error(WrongInfo)
    
    if sys.getsizeof(info) >= conf.INFOMAXSIZE: 
        WrongInfo = (f"网络接口:发送信息不能超过{conf.INFOMAXSIZE}字节 当前Info大小为{sys.getsizeof(info)}字节")
        raise conf.Customization_Error(WrongInfo)
    
    pass
