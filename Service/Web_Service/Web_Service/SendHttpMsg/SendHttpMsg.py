import conf.conf as conf
import sys
import os
import logging
import json

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
        exit()
    else:
        logging.info("参数校验通过")

    #匹配并进行发送信息
    match typ:
        case conf.ORDERMSGREQ:
            info = conf.OrderMsgReq(info)
            ret = WebBase.__MsgBase(url , info)
            retdic = json.loads(ret.text)
            if ret.status_code != 200:
                raise conf.Customization_Error("访问返回状态码非200")
            if retdic["MsgType"] != conf.ORDERMSGRESP:
                raise conf.Customization_Error("错误的回复格式")
            #一切正常
            return retdic["MsgInfo"]
        case _:
            #报错
            print(f"没有类型这样的请求包{type}")
            logging.error(f"没有类型这样的请求包{type}")
            raise conf.Customization_Error("错误的请求包类型")
            

