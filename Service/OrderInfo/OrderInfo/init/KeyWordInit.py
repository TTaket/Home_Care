import logging
import  conf.conf as conf


#需要从conf中读取的内容
#读入文件路径
def KeyWordInit():
    rets = []
    f = open(conf.ORDERINFO_INFILE,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for tmp in flist:
        #跳过所有的空行和注释
        if len(tmp) == 0 or tmp[0] == '#':
            continue;
        else: 
            rets.append(tmp)
    logging.info(f"2.生成的KeyWord信息为:{rets}")
    return rets