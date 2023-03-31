import os

#用户自定义错误
class Customization_Error(RuntimeError):
    def __init__(self , arg):
        self.info = arg
    def __str__(self):
        return str(self.info)

#---------------------Kernel部分
# 目录路径
LOGPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/log/HomeCare_log.txt"

# 用户信息路径
USERINFOPATH = str((os.path.dirname(os.path.abspath(__file__)))) + "/UserInfo.txt"

# 需求文件路径
DEMANDINFOPATH = str((os.path.dirname(os.path.abspath(__file__)))) + "/DemandInfo.txt"

# 关键词路径
KEYWORDPATH = str((os.path.dirname(os.path.abspath(__file__)))) +"/KeyWords.txt"

# BASE路径
BASEPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# CONF路径
CONFPATH = str((os.path.dirname(os.path.abspath(__file__)))) +"/conf.txt"

# kernel的缓冲区
KERNELTMPPATH = BASEPATH+"/Kernel/tmp/"
# kernel缓冲区里文件列表
KERNELTMPFILELIST = BASEPATH+"/Kernel/tmp/FilePaths.txt"
# kernel缓冲区里文件内容
KERNELTMPFILEPATH = BASEPATH+"/Kernel/tmp/Files"

# 临时文件名称
TMPFILE = "tmpfile.txt"

# kernel服务转发
Orderlist = {"吃饭","洗澡"}
locallist = {"音乐","视频"}


#---------------------File_Filter模块
# FF输入缓冲区路径
FF_INPATH = BASEPATH+"/pkg/File_Filter/In"

# FF输出缓冲区路径
FF_OUTPATH = BASEPATH+"/pkg/File_Filter/Out"

# FF文件列表
FF_FILELIST = FF_INPATH+"/Filelist.txt"

# FF文件位置
FF_FILEPATH = FF_INPATH+"/Files/"

# FF临时答案文件
FF_ANSFILE = FF_OUTPATH+"/"+TMPFILE


#---------------------OrderInfo 模块
# OrderInfo输入缓冲区路径
ORDERINFO_INPATH = BASEPATH+"/Service/OrderInfo/In"

# OrderInfo输出缓冲区路径
ORDERINFO_OUTPATH = BASEPATH+"/Service/OrderInfo/Out"

# OrderInfo传入文件位置
ORDERINFO_INFILE = ORDERINFO_INPATH+"/"+TMPFILE

# OrderInfo临时答案文件
ORDERINFO_OUTFILE = ORDERINFO_OUTPATH+"/"+TMPFILE


#---------------------User_OutInfo 模块
# User_OutInfo输入缓冲区路径
USEROUTINFO_INPATH = BASEPATH+"/User/User_OutInfo/In"

# User_OutInfo传入文件位置
USEROUTINFO_INFILE = USEROUTINFO_INPATH+"/"+TMPFILE


#---------------------User_Interact 模块
# User_Interact输入缓冲区路径
USERINTERACT_INPATH = BASEPATH+"/User/User_Interact/In"

# User_Interact输出缓冲区路径
USERINTERACT_OUTPATH = BASEPATH+"/User/User_Interact/Out"

# User_Interact传入文件位置
USERINTERACT_INFILE = USERINTERACT_INPATH+"/"+TMPFILE

# User_Interact临时答案文件
USERINTERACT_OUTFILE = USERINTERACT_OUTPATH+"/"+TMPFILE


#---------------------Web_Service 模块
#定义关键字
ORDERMSGREQ = "1001"
ORDERMSGRESP = "1002"
TypeList = {ORDERMSGREQ}

#定义url
ORDERINFO_URL = "http://43.138.161.192:8080/Order"
UrlList = {ORDERINFO_URL}

#定义信息最大大小 目前为1M
INFOMAXSIZE = 1024*1024

class WebMsg():#用于继承的父类
    MsgType = ""

#订单消息请求与订单消息回复
class OrderMsgReq(WebMsg):
    def __init__(self,dic):
        self.MsgUserID = dic["UserID"]
        self.MsgDemandID = dic["DemandID"]


class OrderMsgResp(WebMsg):
    def __init__(self,info):
        self.MsgInfo = info



