import  Service.Web_Service as Web
import  conf.conf as conf
import  logging
def OrderSend(info):
    try:
        ret = Web.HttpMsg(conf.ORDERINFO_URL , conf.ORDERMSGREQ , info)
    except conf.Customization_Error as err:
        print(err)
        logging.error(err)
    

    return ret