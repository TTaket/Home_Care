# coding=utf-8    
import os
import logging 
import time
import handle 
import interact
from handle.ParameterInvaild import Customization_Error

ANSFILEPATH = "../../out/File_Filter_ans.txt"


#主体运行程序
def Run(Allpath , Keyword):
    #首先进行参数校验
    try:
        handle.ParameterInvaild(Allpath , Keyword)
    except Customization_Error as err:
        logging.error(err.info)
        exit
    else:
        logging.info("参数校验通过")

    #创建并且打开一个存储答案的文档
    fans = open(ANSFILEPATH,'w',encoding='utf-8')    
    logging.info("创建一个存储答案的文档:{}".format(ANSFILEPATH))
    
    Matchallword ={};
    for path in Allpath:
        #打开源文件并且转换为行链表
        f = open(path,encoding='utf-8')
        finfo = f.read()
        logging.info("打开的文件路径:{}".format(os.path.abspath(path)))
        
        #对文本中出现的关键字进行频率调查
        Now_Matchallword = handle.MatchWord(finfo,Keyword)
        #Todo: 存在并发问题 需上锁
        for k,v in Now_Matchallword.items():
            All_num = Matchallword.get(k)
            if  All_num == None:
                Matchallword.update({k:v})
            else:
                Matchallword[k] = Matchallword[k] + v
        f.close()
        

    #对可能关键词进行筛选
    MatchChooseWord = handle.ChooseWord(Matchallword)
    #与用户交互确认答案
    MatchAnsWord = interact.InteractUser(MatchChooseWord)
    #放到答案文件
    datacnt = 1
    for word in  MatchAnsWord:
        DataInfo = str("Data {:>4d}:{}: \tMatchWord:{}".format(datacnt , time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),word))
        fans.write("{}\n".format(DataInfo))
        logging.info("写入答案的数据信息: {}".format(DataInfo))
        datacnt = datacnt +1 
    #关闭所有的文件
    fans.close()
    logging.info("关闭所有的文件")
