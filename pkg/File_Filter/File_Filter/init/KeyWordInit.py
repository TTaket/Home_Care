import logging
import  conf.conf as conf


#读入文件路径
def KeyWordInit():
    KeyWords = []
    f = open(conf.KEYWORDPATH,'r',encoding='utf-8')    
    words = f.read().splitlines()
    for word in words:
        if len(word) == 0 or word[0] == '#':
            continue;
        KeyWords.append(word)
    logging.info(f"2.初始化的关键词为{KeyWords}")
    return KeyWords