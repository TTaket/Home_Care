#设置位置
import  User.User_Interact.User_Interact.InAndOut as InAndOut
import  User.User_Interact.User_Interact.start as start
import  conf.conf as conf

def ChooseWords(src , desc):
    path = src+"/"+conf.TMPFILE
    InAndOut.SetFile(path)
    t = start.Begin()
    start.ChooseWords(t)
    InAndOut.OutFile(desc,conf.TMPFILE)
    start.End()
    
