import logging 

#InteractUser
#用来和用户交互
#return 0 : 验证合法
#return 1 : 验证不合法
def InteractUser_ChooseWords(Words):
    #logging.info("和用户验证的句子: {} , 和用户验证的关键词: {}".format(match_str , match_word))
    logging.info("选择的疑似关键词为关键词 :{}".format(Words))
    
    #占位符添加
    Words.append("sys:当前没有找到需求 如果你想退出请选择 -1")

    RetWord = []
    #对每一个单词疑似关键字进行询问
    for Check_word in Words:
        print ("------------------------\n")
        print ("*您指的行为是   : {}?\n".format(Check_word))
        OK = input("如果是正确的的请键入0 如果是不正确的的请键入1（默认为不合法） 如果需要强制退出请输入-1:")
        if OK == "-1":
            OK = -1
        elif OK != "0":
            OK = 1
        else:
            OK = 0

        print ("你的选择是: {}".format(OK))
        print ("------------------------\n")
        if OK == 0:
            RetWord.append(Check_word)
            #找到第一个匹配的关键词就退出
            break
        if OK == -1:
            RetWord.clear()
            RetWord.append("sys:强制退出")
            #找到第一个匹配的关键词就退出
            break
    
    logging.info("用户确定的单词集合是: {}".format(RetWord))
    return RetWord