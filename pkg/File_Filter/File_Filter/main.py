import start
import InAndOut


def deal(src , desc):
    for path in src:
        InAndOut.SetFile(path)
    t = start.Begin()
    start.Run(t[0] ,t[1])
    InAndOut.OutFile(desc)
    start.End()
    
