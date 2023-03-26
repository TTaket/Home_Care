import pkg.File_Filter.File_Filter.start as start
import pkg.File_Filter.File_Filter.InAndOut as InAndOut
import conf.conf as conf
import logging

def deal(src , desc):
    #独有的方式 src传入的是目录因为里面有多个文件
    for path in src:
        InAndOut.SetFile(path)
    t = start.Begin()
    start.Run(t[0] ,t[1])
    try:
        InAndOut.OutFile(desc,conf.TMPFILE)
    except conf.Customization_Error as err:
        logging.error(err.info)
        print(err.info)
        exit()
    start.End()
    
