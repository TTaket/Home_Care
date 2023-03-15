import time

USERINFOPATH = "../../In/UserInfo.txt"
DEMANDINFOPATH = "../../In/DemandInfo.txt"
def OrderGen(keyword):
    #读取用户信息
    f_User = open(USERINFOPATH , 'r' ,encoding='utf-8' )
    UserID = f_User.read().splitlines()
    UserID = UserID[0][2:]


    #进行匹配需求id
    f_Demand = open(DEMANDINFOPATH , 'r' ,encoding='utf-8' )
    f_Demand_list = f_Demand.read().splitlines()
    Demand_dic = {}
    for tmpinfo in f_Demand_list:
        if len(tmpinfo) == 0 or tmpinfo[0] == '#':
            continue
        else:
            tmplist = tmpinfo.split("-")
            Demand_dic.update({tmplist[1] : tmplist[0]})
    DemandID = Demand_dic[keyword]

    #获取时间
    DateTime = str("{}".format(time.strftime('%y%m%d%H%M%S',time.localtime())))

    #加密
    OrderID = DateTime+UserID+DemandID
    #生成对应订单
    return OrderID