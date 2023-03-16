from . import start
from . import InFile

#对外只提供开始的接口
Begin = start.Begin
#对外提供关闭的接口
End = start.End

#提供InFile 的API
SetKeyWords = InFile.SetKeyWords
SetDemandInfo = InFile.SetDemandInfo
SetFile = InFile.SetFile
SetUserInfo = InFile.SetUserInfo

