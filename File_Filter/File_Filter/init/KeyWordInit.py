import logging

#输入关键词
def KeyWordInit_Mode1():
    logging.info("KeyWordMode 为 交互输入")
    words = []
    while True:
        word = input("请输入关键词并/exit为停止:")
        if word == '/exit':
            break
        else:
            words.append(word)
    print ("用户最后选择的关键词为:{}".format(words))
    logging.info("用户最后选择的关键词为:{}".format(words))
    return words

#读入关键词
def KeyWordInit_Mode2():
   pass