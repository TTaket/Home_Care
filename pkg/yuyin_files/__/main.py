#设置位置
import InAndOut
import start


def deal(src , desc):
    for path in src:
        InAndOut.SetFile(path)
    t = start.Begin()
    start.Run(t[0] ,t[1])
    InAndOut.OutFile(desc)
    start.End()
    
