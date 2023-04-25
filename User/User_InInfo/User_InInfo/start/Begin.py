
import  logging 
import  conf.conf as conf
import  User.User_InInfo.User_InInfo.init as init



#程序运行入口
def Begin():
    
    Keywords = init.KeyWord()
    Files = init.File()

    return Files , Keywords
