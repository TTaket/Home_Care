from . import start
from . import InAndOut
from . import environment


#对外只提供初始化配置的接口
Begin = start.Begin
#对外提供运行的接口
Run = start.Run
#对外提供关闭的接口
End = start.End

#提供导入 的API
SetKeyWords = InAndOut.SetKeyWords
SetDemandInfo = InAndOut.SetDemandInfo
SetFile = InAndOut.SetFile
SetUserInfo = InAndOut.SetUserInfo

#提供清除导入文件的接口
ClearInFile = InAndOut.ClearInFile
ClearOutFile = InAndOut.ClearOutFile

#导出文件 
OutFile = InAndOut.OutFile



