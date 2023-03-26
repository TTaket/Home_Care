# coding=utf-8    
import os
import logging 
import  conf.conf as conf

#修改位置
import  User.User_Interact.User_Interact.handle as handle

#主体运行程序
def ChooseWords(Words):
    #首先进行参数校验
    try:
        handle.ParameterInvaild(Words)
    except conf.Customization_Error as err:
        print (err.info)
        exit()
    else:
        pass

    #创建并且打开一个存储答案的文档
    fans = open(conf.USERINTERACT_OUTFILE,'w',encoding='utf-8')    
    
    #进行关键词搜索
    ret = handle.ChooseWords(Words)

    #进行答案的填装
    for word in ret:
        fans.writelines(word+'\n')

    
    #关闭所有的文件
    fans.close()
    logging.info("5.关闭临时文件")