#---------------------Web_Service 模块
#定义关键字
ORDERMSGREQ = "1001"
ORDERMSGRESP = "1002"
TypeList = {ORDERMSGREQ}

#定义url
ORDERINFO_URL = "http://43.138.161.192:8080/Order"
UrlList = {ORDERINFO_URL}

#定义信息最大大小 目前为1M
INFOMAXSIZE = 1024*1024

class WebMsg():#用于继承的父类
    MsgType = "",
    MsgInfo = ""

#订单消息请求与订单消息回复
class OrderMsgReq(WebMsg):
    def __init__(self,info):
        self.MsgType = ORDERMSGREQ
        self.MsgInfo = info

class OrderMsgResp(WebMsg):
    def __init__(self,info):
        self.MsgType = ORDERMSGRESP
        self.MsgInfo = info



