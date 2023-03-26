import logging 
import re


#MatchWord
#对某一个字符串进行所有关键字的匹配
def MatchWord(NowStr , Keyword):
    logging.info("4.进行匹配的关键词集合： Keyword: {}".format(Keyword))
    Ret= {}
    for NowKeyword in Keyword:
        #捏造出对应的正则表达式匹配句
        TmpRe = NowKeyword
        MatchList = re.findall(TmpRe,NowStr,0)
        tim = len(MatchList)
        if tim != 0:
            Ret.update({NowKeyword : tim})
            logging.info("4.添加关键词:{} 其出现次数：{}".format(NowKeyword , tim))

    logging.info(f"4.匹配结束:结果如下{Ret}")
    return Ret