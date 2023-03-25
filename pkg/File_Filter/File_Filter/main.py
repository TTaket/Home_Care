import pkg.File_Filter.File_Filter.start as start
import pkg.File_Filter.File_Filter.InAndOut as InAndOut
import conf.conf as conf

def deal(src , desc):
    for path in src:
        InAndOut.SetFile(path)
    t = start.Begin()
    start.Run(t[0] ,t[1])
    InAndOut.OutFile(desc,conf.TMPFILE)
    start.End()
    
