import logging 
import conf.conf as conf


#ParameterInvaild
#校验info是否为空
def ParameterInvaild(Info):
    logging.info(f"3.即将校验的Info为{Info}")
    
    #验证info是否为空
    if len(Info) == 0:
        WrongInfo = (f"3.参数校验不合法： Info为空{Info}")
        raise conf.Customization_Error(WrongInfo) 

    logging.info("3.参数校验一切正常")
    #一切正常
    pass
