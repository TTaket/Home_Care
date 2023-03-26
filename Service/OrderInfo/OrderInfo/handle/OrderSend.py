import  Service.Web_Service as Web
import  conf.conf as conf
import  logging
def OrderSend(info):
    logging.info(f"5.准备发送信息{info}")
    try:
        ret = Web.HttpMsg(conf.ORDERINFO_URL , conf.ORDERMSGREQ , info)
    except conf.Customization_Error as err:
        print(err)
        logging.error(err)
        exit()
    

    return ret