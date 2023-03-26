import os
import logging 
import conf.conf as conf


#ParameterInvaild
#检验传入的关键词集合是否为空
def ParameterInvaild(Words):
    logging.info(f"3.即将校验的Words为{Words}")
    
    #验证info是否为空
    if len(Words) == 0:
        WrongInfo = (f"3.参数校验不合法： Words为空{Words}")
        raise conf.Customization_Error(WrongInfo) 

    logging.info("3.参数校验一切正常")
    #一切正常