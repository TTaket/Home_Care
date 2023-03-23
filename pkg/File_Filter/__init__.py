from . import File_Filter

#提供 启动相关 的API
Begin = File_Filter.Begin
Run = File_Filter.Run
End = File_Filter.End

#提供InFile 的API
SetFile = File_Filter.SetFile

#清除 导入缓冲区
ClearInFile = File_Filter.ClearInFile
#清除 导出缓冲区
ClearOutFile = File_Filter.ClearOutFile

#设置导出文件API
OutFile = File_Filter.OutFile

