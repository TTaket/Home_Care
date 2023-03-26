#设置位置
import  User.User_Interact.User_Interact.InAndOut as InAndOut
import  User.User_Interact.User_Interact.start as start
import  conf.conf as conf
import  logging

def ChooseWords(srcfile , descpath):
    logging.info("-----进入UserInteract ChooseWords部分-----")
    path = srcfile
    InAndOut.SetFile(path)
    t = start.Begin()
    start.ChooseWords(t)
    try:
        InAndOut.OutFile(descpath,conf.TMPFILE)
    except conf.Customization_Error as err:
        print(err.info)
        logging.error(err.info)
        exit()
    
    start.End()
    
