import  Service.Web_Service as Web
import  conf.conf as conf
import  logging
def OrderSend(dic):
    logging.info(f"5.准备发送信息{dic}")
    try:
        ret = Web.HttpMsg( conf.ORDERMSGREQ , dic)
    except conf.Customization_Error as err:
        print(err)
        logging.error(err)
        exit()
    

    return ret