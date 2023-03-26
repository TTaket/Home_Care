#设置位置
import  User.User_OutInfo.User_OutInfo.InAndOut as InAndOut
import  User.User_OutInfo.User_OutInfo.start as start
import  conf.conf as conf
import  logging

def OutInfo(srcfile):
    logging.info("-----进入UserOutInfo OutInfo部分-----")
    path = srcfile
    InAndOut.SetFile(path)
    lis = start.Begin()
    start.ChooseWords(lis)
    start.End()
    
