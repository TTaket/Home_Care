import  conf.conf as conf
import logging

def DemandInfoInit():
    f_Demand = open(conf.DEMANDINFOPATH , 'r' ,encoding='utf-8' )
    f_Demand_list = f_Demand.read().splitlines()
    DemandInfo_dic = {}
    for tmpinfo in f_Demand_list:
        #跳过所有的空行和注释
        if len(tmpinfo) == 0 or tmpinfo[0] == '#':
            continue
        else:
            tmplist = tmpinfo.split("-")
            DemandInfo_dic.update({tmplist[1] : tmplist[0]})
    logging.info(f"2.生成的DemandInfo信息为:{DemandInfo_dic}")
    return DemandInfo_dic