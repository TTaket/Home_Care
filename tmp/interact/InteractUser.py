import logging 

#InteractUser
#用来和用户交互
#return 0 : 验证合法
#return 1 : 验证不合法
def InteractUser(match_chooseword):
    #logging.info("和用户验证的句子: {} , 和用户验证的关键词: {}".format(match_str , match_word))
    logging.info("选择的疑似关键词为关键词 :{}".format(match_chooseword))

    RetWord = []
    #对每一个单词疑似关键字进行询问
    
    for Check_word in match_chooseword:
        print ("------------------------\n")
        print ("*您指的行为是   : {}?\n".format(Check_word))
        OK = input("如果是正确的的请键入0 如果是不正确的的请键入1（默认为不合法）:")
        if OK != "0":
            OK = 1
        else:
            OK = 0
            RetWord.append(Check_word)
            #找到第一个匹配的关键词就退出
            break
        print ("你的选择是: {}".format(OK))
        print ("------------------------\n")
    
    logging.info("用户确定的单词集合是: {}".format(RetWord))
    return RetWord