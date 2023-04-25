import conf.conf as conf
import requests
import logging
from urllib import parse
import json

def __MsgBase(url , Msg):
    #把类信息变成字典发送过去
    #HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8', 'Key': '332213fa4a9d4288b5668ddd9'}
    # key 代表浏览器的原生 form 表单
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    data = parse.urlencode(Msg.__dict__)
    logging.info(f"网络接口被调用:要求发送信息为{data}")
    Resp = requests.post(url , headers=HEADERS, data=data).text
    logging.info(f"网络接口被调用:返回信息为header:{Resp.headers},status_code:{Resp.status_code},json:{json.loads(Resp.text)}")
    return Resp

        
# import requests
# import logging
# from urllib import parse
# import json

# class WebMsg():#用于继承的父类
#     MsgType = ""

# class WebMsgReq(WebMsg):
#     def __init__(self,dic):
#         self.user_id = dic["UserID"]
#         self.requirement_id = dic["DemandID"]


# def __MsgBase():
#     #把类信息变成字典发送过去
#     url = "http://123.57.187.239:8000/api/person/postRobotOrderInfo/"
#     Msg = WebMsgReq({'UserID':'2104010201' , 'DemandID':'101'})
#     #HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8', 'Key': '332213fa4a9d4288b5668ddd9'}
#     # key 代表浏览器的原生 form 表单
#     HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
#     data = parse.urlencode(Msg.__dict__)
#     #logging.info(f"网络接口被调用:要求发送信息为{data}")
#     print ("----------------")
#     Resp = requests.post(url , headers=HEADERS, data=data).text
#     print ("----------------")
#     #retdic = json.loads(Resp.text)
#     print (Resp)
# __MsgBase()