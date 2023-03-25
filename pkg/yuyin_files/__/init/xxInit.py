import logging
import  conf.conf as conf


#需要从conf中读取的内容
#读入文件路径
def xxInit():
    rets = []
    f = open(conf.xx,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for tmp in flist:
        if len(tmp) == 0 or tmp[0] == '#':
            continue;
        rets.append(tmp)
    return rets