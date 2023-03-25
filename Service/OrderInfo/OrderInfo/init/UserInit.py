import  conf.conf as conf
import logging

#读取用户信息
#目前只返回用户ID
def UserInfoInit():
    f_User = open(conf.USERINFOPATH , 'r' ,encoding='utf-8' )
    f_User_list = f_User.read().splitlines()
    UserInfo_dic = {}
    for tmpinfo in f_User_list:
        if len(tmpinfo) == 0 or tmpinfo[0] == '#':
            continue
        else:
            tmplist = tmpinfo.split("-")
            UserInfo_dic.update({tmplist[0] : tmplist[1]})
    logging.info("生成的UserInfo信息为:",UserInfo_dic)
    return UserInfo_dic