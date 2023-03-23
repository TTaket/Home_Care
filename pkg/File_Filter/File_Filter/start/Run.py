# coding=utf-8    
import os
import logging 
import handle 
import conf
from conf import Customization_Error 


#主体运行程序
def Run(Begin_dic):
    #拆包
    FilePaths =  Begin_dic.FilePaths
    Keywords = Begin_dic.KeyWords
     
    #首先进行参数校验
    try:
        handle.ParameterInvaild(FilePaths , Keywords)
    except Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit
    else:
        logging.info("参数校验通过")

    #创建并且打开一个存储答案的文档
    fans = open(conf.ANSFILEPATH,'w',encoding='utf-8')    
    logging.info("创建一个存储答案的文档:{}".format(conf.ANSFILEPATH))
    
    Matchallword ={};
    for path in FilePaths:
        #打开导入文件
        f = open(path,'r',encoding='utf-8')
        finfo = f.read()
        logging.info("打开的文件路径:{}".format(os.path.abspath(path)))
        
        #对文本中出现的关键字进行频率调查
        Now_Matchallword = handle.MatchWord(finfo,Keywords)
        #Todo: 存在并发问题 需上锁
        for k,v in Now_Matchallword.items():
            All_num = Matchallword.get(k)
            if  All_num == None:
                Matchallword.update({k:v})
            else:
                Matchallword[k] = Matchallword[k] + v
        f.close()
        

    #对可能关键词进行筛选
    #暂时停用-所有匹配的关键词直接进行提问 无需筛选
    #MatchChooseWord = handle.ChooseWord(Matchallword)
    MatchChooseWord = Matchallword.keys()

    if len(MatchChooseWord) == 0:
        return False
    else:
        for word in MatchChooseWord:
            fans.write("{}\n".format(word))
            logging.info("FF找到的关键词有: {}".format(word))
    
    
    #关闭所有的文件
    fans.close()
    logging.info("关闭所有的文件")
    return True
