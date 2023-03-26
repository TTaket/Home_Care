#设置位置
import Service.OrderInfo.OrderInfo.InAndOut as InAndOut
import Service.OrderInfo.OrderInfo.start as start
import conf.conf as conf
import logging

def OrderInfo(src , desc):
    logging.info("-----进入OrderInfo OrderInfo部分-----")
    InAndOut.SetFile(src)
    t = start.Begin()
    ret = start.Run(t[0] , t[1] , t[2])
    try:
        InAndOut.OutFile(desc , conf.TMPFILE)
    except conf.Customization_Error as err:
        print(err.info)
        logging.error(err.info)
        exit()
    start.End()
    #向内核返回ret的内容
    return ret
    
