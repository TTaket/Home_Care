from . import start
from . import InAndOut



#对外只提供初始化配置的接口
Begin = start.Begin
#对外提供运行的接口
Run = start.Run
#对外提供关闭的接口
End = start.End

#提供导入 的API
SetKeyWords = InAndOut.SetKeyWords
SetFile = InAndOut.SetFile

#提供清除导入文件的接口
ClearInFile = InAndOut.ClearInFile
ClearOutFile = InAndOut.ClearOutFile

#导出文件 
OutFile = InAndOut.OutFile



