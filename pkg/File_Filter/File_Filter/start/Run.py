# coding=utf-8    
import os
import logging 
import  pkg.File_Filter.File_Filter.handle as handle
import  conf.conf as conf


#主体运行程序
def Run(Files,Keywords):
    #拆包
    FilePaths = Files
    #首先进行参数校验
    try:
        handle.ParameterInvaild(FilePaths , Keywords)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print (err.info)
        exit()
    else:
        pass

    #创建并且打开一个存储答案的文档
    fans = open(conf.FF_ANSFILE,'w',encoding='utf-8')    
    
    Matchallword ={};
    for path in FilePaths:
        #打开导入文件
        f = open(path,'r',encoding='utf-8')
        finfo = f.read()
        #对文本中出现的关键字进行频率调查
        Now_Matchallword = handle.MatchWord(finfo,Keywords)

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

    for word in MatchChooseWord:
        fans.write("{}\n".format(word))
        logging.info("5.FF找到的关键词有: {}".format(word))
    
    #关闭所有的文件
    fans.close()
    logging.info("5.关闭文件")
