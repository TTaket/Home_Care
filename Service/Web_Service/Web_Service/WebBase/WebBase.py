import conf.conf as conf
import requests
import json

def __MsgBase(url , info):
    param = "吃饭"
    Resp = requests.post(url , param.encode())
    print(Resp.json)
    return Resp

    