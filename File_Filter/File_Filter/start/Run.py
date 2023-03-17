# coding=utf-8    
import os
import logging 
import handle 
import interact
import conf
from conf import Customization_Error 


#主体运行程序
def Run(Begin_dic):
    #拆包
    FilePaths =  Begin_dic.FilePaths
    Keywords = Begin_dic.KeyWords
    UserInfo_dic =Begin_dic.UserInfo
    DemandInfo_dic = Begin_dic.DemandInfo
     
    #首先进行参数校验
    try:
        handle.ParameterInvaild(FilePaths , Keywords ,UserInfo_dic , DemandInfo_dic)
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

    #与用户交互确认答案
    MatchAnsWord = interact.UserChoose(MatchChooseWord)
    
    if MatchAnsWord == []:
        #本轮匹配没有匹配到信息
        #print ("本轮匹配没有匹配到合法的关键词 请您重新进行语音输入")
        print ("本轮并没有匹配到信息")
        logging.info("没有匹配到信息")
        return False
    else:
        #本轮匹配匹配到信息 即将放到答案文件
        try:
            OrderInfo = handle.OrderGen(MatchAnsWord[0] ,UserInfo_dic , DemandInfo_dic)
        except Customization_Error as err:
            logging.error(err.info)
            print (err.info)
            exit
        else:
            print ("订单号生成成功")
            logging.info("订单号生成成功")
        fans.write("{}\n".format(OrderInfo))
        logging.info("即将发送的数据信息: {}".format(OrderInfo))
    
    # 多个请求一同处理
    # 暂时停用
    # datacnt = 1
    # for word in  MatchAnsWord:
    #     DataInfo = str("Data {:>4d}:{}: \tMatchWord:{}".format(datacnt , time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),word))
    #     fans.write("{}\n".format(DataInfo))
    #     logging.info("写入答案的数据信息: {}".format(DataInfo))
    #     datacnt = datacnt +1 
    
    #关闭所有的文件
    fans.close()
    logging.info("关闭所有的文件")
    return True
