#设置位置
import Home_care.User.User_Interact.User_Interact.InAndOut as InAndOut
import Home_care.User.User_Interact.User_Interact.start as start
import Home_care.conf.conf as conf

def ChooseWords(src , desc):
    for path in src:
        InAndOut.SetFile(path)
    t = start.Begin()
    start.ChooseWords(t[0])
    InAndOut.OutFile(desc,conf.TMPFILE)
    start.End()
    
