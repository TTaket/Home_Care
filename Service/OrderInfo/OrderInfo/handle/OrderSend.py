import Home_care.Service.Web_Service as Web
import Home_care.conf.conf as conf

def OrderSend(info , url ):
    ret = Web.HttpMsg(url , conf.ORDERMSGREQ , info)
    return ret