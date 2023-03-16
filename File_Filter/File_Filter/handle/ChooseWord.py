import logging 


#ChooseWord
#对这个匹配字典里面进行筛选

#——>传入关键词集合 
#<——返回选中的单词
def ChooseWord(Match_allword):
    logging.info("匹配的关键词以及频率如下 :{}".format(Match_allword))
    Ret= []

    #在单词集合中找到想要符合高频率的单词
    #自定义匹配规则 目前匹配规则是出现3次及以上的单词
    for NowKeyword,NowTime in Match_allword.items():
        if NowTime>=1 : 
            Ret.append(NowKeyword)
            logging.info("添加疑似关键词{}".format(NowKeyword) )
    return Ret