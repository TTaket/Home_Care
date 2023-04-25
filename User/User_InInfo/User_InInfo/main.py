
import  logging 
import  conf.conf as conf
import  User.User_InInfo.User_InInfo.InAndOut as InAndOut
import  User.User_InInfo.User_InInfo.start as start


def deal(desc):
    logging.info("-----进入UserInInfo InInfo部分-----")
    #把调用语音读入 读入到本地的缓冲区
    #解析缓冲区内容写入日志
    start.Run()
    
    #把文件放入到 本地的输出缓冲区中 并且 把输出缓冲区放到中心缓冲区
    InAndOut.OutFile(desc,conf.TMPFILE)

    #清楚缓冲区空间 
    start.End()

    
    
    
    
