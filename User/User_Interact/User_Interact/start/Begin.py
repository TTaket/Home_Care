import logging 
import Home_care.conf.conf as conf


#修改位置
import Home_care.User.User_Interact.User_Interact.init as init 



#程序初始化
def Begin():
    print ("Begin初始配置开始")
    #初始化
    File = init.File()
    
    print ("File初始化结果{}".format(File))
    logging.info("File初始化结果{}".format(File))

    return File
