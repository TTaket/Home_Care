import os
class WebMsg():
    MsgType = "",
    MsgInfo = ""

#定义关键字
ORDERMSGREQ = 1001
TypeList = {ORDERMSGREQ}

#定义url
TESTURL = "xxx"
UrlList = {TESTURL}

#定义信息最大大小 目前为1M
INFOMAXSIZE = 1024*1024

#自定义错误
class Customization_Error(RuntimeError):
    def __init__(self , arg):
        self.info = arg
    def __str__(self):
        return str(self.info)
    

#订单消息请求与订单消息回复
class OrderMsgReq(WebMsg):
    def __init__(self,info):
        self.MsgType = "OrderMsgReq"
        self.MsgInfo = info

class OrderMsgResp(WebMsg):
    def __init__(self,info):
        self.MsgType = "OrderMsgResp"
        self.MsgInfo = info



# 目录路径
LOGPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/log/Web_Service_log.txt"

# BASE路径
BASEPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
