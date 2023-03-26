#设置位置
import Service.OrderInfo.OrderInfo.InAndOut as InAndOut
import Service.OrderInfo.OrderInfo.start as start
import conf.conf as conf


def deal(src , desc):
    InAndOut.SetFile(src)
    t = start.Begin()
    ret = start.Run(t[0] , t[1] , t[2])
    InAndOut.OutFile(desc , conf.TMPFILE)
    start.End()
    #向内核返回ret的内容
    return ret
    
