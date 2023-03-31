import conf.conf as conf
import requests
import logging
import json

def __MsgBase(url , Msg):
    #把类信息变成字典发送过去
    logging.info(f"网络接口被调用:要求发送信息为{Msg.__dict__}")
    Resp = requests.post(url , json= Msg.__dict__)
    logging.info(f"网络接口被调用:返回信息为header:{Resp.headers},status_code:{Resp.status_code},json:{json.loads(Resp.text)}")
    return Resp

        