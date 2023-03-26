import logging 

#把内容打印到用户终端
def User_OutInfo(Info):
    #把信息打印到终端
    logging.info(f"4.打印到终端的内容为{Info}")
    print(f"<打印到用户终端内容：{Info}>")
    