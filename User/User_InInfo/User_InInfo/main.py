#设置位置
import Home_care.User.User_InInfo.User_InInfo.InAndOut as InAndOut
import Home_care.User.User_InInfo.User_InInfo.start as start


def deal(desc):
    start.Run()
    InAndOut.OutFile(desc)
    start.End()
    
