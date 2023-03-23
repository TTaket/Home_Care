#与用户交互确认答案
    MatchAnsWord = interact.UserChoose(MatchChooseWord)
    
    if MatchAnsWord == []:
        #本轮匹配没有匹配到信息
        #print ("本轮匹配没有匹配到合法的关键词 请您重新进行语音输入")
        print ("本轮并没有匹配到信息")
        logging.info("没有匹配到信息")
        return False
    else:
        #本轮匹配匹配到信息 即将放到答案文件
        try:
            OrderInfo = handle.OrderGen(MatchAnsWord[0] ,UserInfo_dic , DemandInfo_dic)
        except Customization_Error as err:
            logging.error(err.info)
            print (err.info)
            exit
        else:
            print ("订单号生成成功")
            logging.info("订单号生成成功")
        fans.write("{}\n".format(OrderInfo))
        logging.info("即将发送的数据信息: {}".format(OrderInfo))
    
    # 多个请求一同处理
    # 暂时停用
    # datacnt = 1
    # for word in  MatchAnsWord:
    #     DataInfo = str("Data {:>4d}:{}: \tMatchWord:{}".format(datacnt , time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),word))
    #     fans.write("{}\n".format(DataInfo))
    #     logging.info("写入答案的数据信息: {}".format(DataInfo))
    #     datacnt = datacnt +1 