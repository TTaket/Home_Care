import logging 

LOGPATH = '../../log/File_Filter_log.txt'
#初始化整个日志系统
def LogInit():
    #配置基本信息
    logging.basicConfig(
            filename = LOGPATH,
            format = '%(asctime)s - %(levelname)s  %(funcName)s : %(message)s',
            filemode = "w",
            level = logging.INFO, 
            encoding='utf-8'
        )
