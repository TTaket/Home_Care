import logging
import Home_care.conf.conf as conf


#需要从conf中读取的内容
#读入文件路径
def KeyWordInit():
    rets = []
    f = open(conf.ORDERINFO_INFILE,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for tmp in flist:
        if len(tmp) == 0 or tmp[0] == '#':
            continue;
        rets.append(tmp)
    return rets