import logging 
import re


#MatchWord
#对某一个字符串进行所有关键字的匹配

#——>传入字符串和关键词集合 
#<——返回匹配成功的关键词集合以及出现次数
def MatchWord(NowStr , Keyword):
    logging.info("传入的关键词集合： Keyword: {}".format( Keyword))
    Ret= {}
    for NowKeyword in Keyword:
        #捏造出对应的正则表达式匹配句
        TmpRe = NowKeyword
        MatchList = re.findall(TmpRe,NowStr,0)
        tim = len(MatchList)
        if tim != 0:
            Ret.update({NowKeyword : tim})
            logging.info("添加关键词:{} 其出现次数：{}".format(NowKeyword , tim))

    #print ("-----------------------")
    return Ret