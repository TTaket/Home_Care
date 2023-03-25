import os
import logging 
import  conf.conf as conf


#ParameterInvaild
#
#
def ParameterInvaild(KeyWords):
    logging.info("KeyWords: {}".format(KeyWords))
    #验证KeyWords是否非空
    if len(KeyWords) == 0:
        raise conf.Customization_Error(f"参数校验不合法： KeyWords为空 {KeyWords}") 
    
    #一切正常
    pass
