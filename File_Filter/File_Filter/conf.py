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

class Begin_Info():
    FilePaths = {},
    KeyWords = {},
    UserInfo = {},
    DemandInfo = {},



# 输入文件路径
FILEPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/In/FilePaths.txt"

# 真实文件位置
FILESPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/In/Files/"

# 输出订单号路径
ANSFILEPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/Out/File_Filter_ans.txt"

# 目录路径
LOGPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/log/File_Filter_log.txt"

# 用户信息路径
USERINFOPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/In/UserInfo.txt"

# 需求文件路径
DEMANDINFOPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/In/DemandInfo.txt"

# 关键词路径
KEYWORDPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) +"/In/KeyWords.txt"

# BASE路径
BASEPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 输入缓冲区路径
INDIRPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ "/In/"

# 输出缓冲区路径
OUTDIRPATH = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/Out/"

