from . import start
from . import InFile
from . import environment


#对外只提供初始化配置的接口
Begin = start.Begin
#对外提供运行的接口
Run = start.Run
#对外提供关闭的接口
End = start.End

#提供InFile 的API
SetKeyWords = InFile.SetKeyWords
SetDemandInfo = InFile.SetDemandInfo
SetFile = InFile.SetFile
SetUserInfo = InFile.SetUserInfo

#提供清除导入文件的接口
Clear = InFile.ClearInFile


