import logging 

#InteractUser
#传入单词集合
#返回需求
def ChooseWords(Words):
    #占位符添加
    Words.append("sys:当前没有找到需求 如果你想退出请选择 -1")
    logging.info(f"4.选择的疑似需求集合 :{Words}")

    #创建返回数组
    RetWord = []

    #对每一个单词疑似关键字进行询问
    for Check_word in Words:
        print ("------------------------\n")
        print (f"*您指的行为是   : {Check_word}?\n")
        OK = input("如果是正确的的请键入0 如果是不正确的的请键入1（默认为不合法） 如果需要强制退出请输入-1:")
        if OK == "-1":#强制退出
            OK = -1
        elif OK != "0":#不正确
            OK = 1
        else:#正确
            OK = 0
        print (f"你的选择是: {OK}")
        print ("------------------------\n")

        if OK == 0:
            RetWord.append(Check_word)#找到了匹配的信息
            break
        if OK == -1:#找到了强制退出
            RetWord.append("sys:强制退出")
            break
    
    logging.info(f"4.用户确定的需求是: {RetWord}")
    return RetWord