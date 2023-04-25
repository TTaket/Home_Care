import logging
import pkg as pkg 
import conf.conf as conf
import re
import os
import time

#InteractUser
#传入单词集合
#返回需求
def ChooseWords(Words):
    #占位符添加
    if len(Words) == 0:
        Words.append("sys:当前没有找到需求 如果你想退出请选择 -1")
        logging.info(f"4.选择的疑似需求集合 :{Words}")

    #创建返回数组
    RetWord = []

    #对每一个单词疑似关键字进行询问
    # for Check_word in Words:
    #     print ("------------------------\n")
    #     print (f"*您指的行为是   : {Check_word}?\n")
    #     OK = input("如果是正确的的请键入0 如果是不正确的的请键入1（默认为不合法） 如果需要强制退出请输入-1:")
    #     if OK == "-1":#强制退出
    #         OK = -1
    #     elif OK != "0":#不正确
    #         OK = 1
    #     else:#正确
    #         OK = 0
    #     print (f"你的选择是: {OK}")
    #     print ("------------------------\n")

    #     if OK == 0:
    #         RetWord.append(Check_word)#找到了匹配的信息
    #         break
    #     if OK == -1:#找到了强制退出
    #         RetWord.append("sys:强制退出")
    #         break

    for Check_word in Words:
        print ("------------------------\n")
        print (f"*您指的行为是   : {Check_word}?\n")
        Sflag = 0;
        OK = 0;
        time.sleep(2);
        while(Sflag == 0):
            pkg.StoT(conf.USERINTERACT_INPATH);
            if ((os.path.exists(conf.USERINTERACT_INFILE) == False) or (os.path.getsize(conf.USERINTERACT_INFILE) == 0)):
                #if os.path.exists(conf.USERINERACT_INFILE) == False :
                #    print("worry 1")
                #if os.path.getsize(conf.USERINTERACT_INFILE) :
                #    print("worry 2")
                print("语音读入失败 未生成文件或文件长度为0")
                continue;
            else:
                Sflag = 1;


            rfile = open(conf.USERINTERACT_INFILE , 'r' , encoding='utf-8')
            rstr = rfile.read();        
            flag_exit =len(re.findall("退出",rstr))
            flag_no =len(re.findall("不是",rstr))
            flag_yes =len(re.findall("是",rstr)) + len(re.findall("使",rstr)) + len(re.findall("轼" , rstr)) + len(re.findall("好的",rstr)) + len(re.findall("没错",rstr))
            if flag_exit:
                OK = 3
            elif flag_no:#不是
                OK = 2
            elif flag_yes:#正确
                OK = 1
            print (f"你的选择是: {OK}")
            print ("------------------------\n")

            if OK == 1:
                RetWord.append(Check_word)#找到了匹配的信息
                break
            if OK == 2:#不是
                continue
            if OK == 3:#找到了强制退出
                RetWord.append("sys:强制退出")
                break
            else:
                print ("没听清您的选择");
                Sflag = 0;

    
    logging.info(f"4.用户确定的需求是: {RetWord}")
    return RetWord
