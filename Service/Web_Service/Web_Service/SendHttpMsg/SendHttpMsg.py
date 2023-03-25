import conf.conf as conf
import sys
import os
import logging

#增加包路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import Service.Web_Service.Web_Service.WebBase as WebBase
import Service.Web_Service.Web_Service.SendHttpMsg.ParameterInvaild as ParameterInvaild

def SendHttpMsg(url , typ , info):
    
    #进行参数校验
    try:
        ParameterInvaild.Check(url , typ , info)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit
    else:
        logging.info("参数校验通过")

    #匹配并进行发送信息
    info = ""
    match typ:
        case conf.ORDERMSGREQ:
            info = conf.OrderMsgReq(info)
            info = WebBase.__MsgBase(url , info)
        case _:
            #报错
            print(f"没有类型这样的请求包{type}")
            logging.error(f"没有类型这样的请求包{type}")
            exit

    
    #信息处理之后返回
    return info
