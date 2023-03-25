import logging
import conf.conf as conf
import sys

def Check(url , typ , info):
    if typ not in conf.TypeList:
        logging.info(f"不存在这种信息类型:{typ}")
        raise conf.Customization_Error(f"不存在这种信息类型{typ}")
    if url not in conf.UrlList:
        logging.info(f"不存在这个URL:{url}")
        raise conf.Customization_Error(f"不存在这个URL:{url}")
    
    #info不为空
    if sys.getsizeof(info) == 0: 
        logging.info(f"发送信息不能为空 当前Info大小为{sys.getsizeof(info)}字节")
        raise conf.Customization_Error(f"发送信息不能为空 当前Info大小为{sys.getsizeof(info)}字节")
    
    if sys.getsizeof(info) == 0: 
        logging.info(f"发送信息不能超过{conf.INFOMAXSIZE}字节 当前Info大小为{sys.getsizeof(info)}字节")
        raise conf.Customization_Error(f"发送信息不能超过{conf.INFOMAXSIZE}字节 当前Info大小为{sys.getsizeof(info)}字节")
    
    pass
