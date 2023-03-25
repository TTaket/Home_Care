#设置位置
import Home_care.Service.OrderInfo.OrderInfo.InAndOut as InAndOut
import Home_care.Service.OrderInfo.OrderInfo.start as start


def deal(src , url):
    for path in src:
        InAndOut.SetFile(path)
    t = start.Begin()
    ret = start.Run(t[0] , t[1] , t[2] , url)
    start.End()
    #向内核返回ret的内容
    return ret
    
