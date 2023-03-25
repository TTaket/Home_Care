import  Service.Web_Service as Web
import  conf.conf as conf

def OrderSend(info , url ):
    ret = Web.HttpMsg(url , conf.ORDERMSGREQ , info)
    return ret