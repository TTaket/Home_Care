# coding=utf-8    
import os
import logging 
import  conf.conf as conf

#修改位置
import handle 

#主体运行程序
def Run(xx, yy):
    
    
    #首先进行参数校验
    try:
        handle.ParameterInvaild(xx , yy)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit
    else:
        logging.info("参数校验通过")

    #创建并且打开一个存储答案的文档
    fans = open(conf.xx_ANSFILE,'w',encoding='utf-8')    
    
   
    
    #关闭所有的文件
    fans.close()
    logging.info("关闭文件")
    return True
