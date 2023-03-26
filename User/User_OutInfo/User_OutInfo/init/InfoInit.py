import logging
import  conf.conf as conf


#读入文件路径
def InfoInit():
    Info = []
    f = open(conf.USEROUTINFO_INFILE,'r',encoding='utf-8')    
    flist = f.read().splitlines()
    for info in flist:
        #跳过注释的内容和空行
        if len(info) == 0 or info[0] == '#':
            continue;
        Info.append(info)
    logging.info(f"2.初始化的info内容为{info}")
    return Info