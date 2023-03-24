import os

#用户自定义错误
#Customization error
#Using: 
#    Customization_Error(problem)
class Customization_Error(RuntimeError):
    def __init__(self , arg):
        self.info = arg
    def __str__(self):
        return str(self.info)



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

#---------------------File_Filter模块
# FF输入缓冲区路径
FF_INPATH = BASEPATH+"/pkg/File_Filter/In"

# FF输出缓冲区路径
FF_OUTPATH = BASEPATH+"/pkg/File_Filter/Out"

# FF文件列表
FF_FILELIST = FF_INPATH+"/Filelist"

# FF文件位置
FF_FILEPATH = FF_INPATH+"/File"

# FF临时答案文件
FF_ANSFILE = FF_OUTPATH+"/AnsFile.txt"


