import conf.conf as conf
import logging

#读入文件路径
def WordInit():
    Words = []
    f = open(conf.USERINTERACT_INFILE,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for word in flist:
        #跳过空行和注释
        if len(word) == 0 or word[0] == '#':
            continue;
        Words.append(word)
    logging.info(f"2.初始化的Words内容为{Words}")
    return Words