import conf
import requests

def __MsgBase(url , info):
    Resp = requests.post(url , info)
    return Resp

    