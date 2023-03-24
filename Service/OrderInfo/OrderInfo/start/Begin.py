import logging 
import Home_care.conf.conf as conf


#修改位置
import init



#程序初始化
def Begin():
    print ("Begin初始配置开始")
    #初始化
    xx = init.xxinit()
    
    print ("xx初始化结果{}".format(xx))
    logging.info("xx初始化结果{}".format(xx))

    return xx
