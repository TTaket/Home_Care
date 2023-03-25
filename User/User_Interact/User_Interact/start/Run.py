# coding=utf-8    
import os
import logging 
import Home_care.conf.conf as conf

#修改位置
import Home_care.User.User_Interact.User_Interact.handle as handle

#主体运行程序
def ChooseWords(KeyWords):
    #首先进行参数校验
    try:
        handle.ParameterInvaild(KeyWords)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit
    else:
        logging.info("参数校验通过")

    #创建并且打开一个存储答案的文档
    fans = open(conf.USERINTERACT_OUTFILE,'w',encoding='utf-8')    
    
    ret = handle.ChooseWords(KeyWords)

    for word in ret:
        fans.writelines(word+'\n')

    
    #关闭所有的文件
    fans.close()
    logging.info("关闭文件")
    return True