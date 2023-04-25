#设置位置
import conf.conf as conf
import pkg.SpeechAndText.SpeechAndText.InAndOut as InAndOut
import pkg.SpeechAndText.SpeechAndText.start as start

#自动录音并且送回到中心缓冲区
def StoT(desc):
    #t = start.Begin()
    start.StoT()
    InAndOut.OutFile(desc,conf.TMPFILE)
    start.End()
    
