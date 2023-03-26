import conf.conf as conf
import requests
import logging
import json

def __MsgBase(url , info):
    #把类信息变成字典发送过去
    logging.info(info.__dict__)
    Resp = requests.post(url , json= info.__dict__)
    return Resp

    