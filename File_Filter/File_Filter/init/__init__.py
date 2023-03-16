#init中主要是初始化
from . import LogInit
from . import FileInit
from . import KeyWordInit
from . import DemandInit
from . import UserInit


#日志初始化
Log = LogInit.LogInit

#文件初始化
#1 交互式读入 
#2 文件读入
File_Mode1 = FileInit.FileInit_Mode1
File_Mode2 = FileInit.FileInit_Mode2

#关键词初始化
#1 交互式读入 
#2 文件读入
KeyWord_Mode1 = KeyWordInit.KeyWordInit_Mode1
KeyWord_Mode2 = KeyWordInit.KeyWordInit_Mode2

#用户信息初始化
UserInfo = UserInit.UserInfoInit

#需求字典初始化
DemandInfo = DemandInit.DemandInfoInit