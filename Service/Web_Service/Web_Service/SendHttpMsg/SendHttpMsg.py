import conf.conf as conf
import sys
import os
import logging
import json

import Service.Web_Service.Web_Service.WebBase as WebBase
import Service.Web_Service.Web_Service.SendHttpMsg.ParameterInvaild as ParameterInvaild

def SendHttpMsg(typ , dic):
    
    #进行参数校验
    try:
        ParameterInvaild.Check(typ , dic)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit()
    else:
        pass

    #匹配并进行发送信息
    match typ:
        case conf.ORDERMSGREQ:
            #Msg = conf.OrderMsgReq(dic)
            #translate to website REQ
            Msg = conf.WebMsgReq(dic)
            resp = WebBase.__MsgBase(conf.ORDERINFO_URL , Msg)
            retdic = eval(resp)
#           if resp.status_code != 200:
#               print (resp.stauts_code , resp.text)
#               raise conf.Customization_Error("访问返回状态码非200")
            #一切正常
            return retdic["result"]
        case _:
            #报错
            WrongInfo = (f"没有类型这样的请求包{type}")
            print(WrongInfo)
            logging.error(WrongInfo)
            raise conf.Customization_Error(WrongInfo)
            

