import  pkg.File_Filter.File_Filter.InAndOut as InAndOut

def End():
    #卸载所有导入文件
    InAndOut.ClearInFile()
    InAndOut.ClearOutFile()