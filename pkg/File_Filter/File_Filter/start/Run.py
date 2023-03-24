# coding=utf-8    
import os
import logging 
import Home_care.pkg.File_Filter.File_Filter.handle as handle
import Home_care.conf.conf as conf


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
        exit
    else:
        logging.info("参数校验通过")

    #创建并且打开一个存储答案的文档
    fans = open(conf.FF_ANSFILE,'w',encoding='utf-8')    
    
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
    logging.info("关闭文件")
    return True
