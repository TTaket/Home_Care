#handle中是主要的处理函数
from . import ChooseWord
from . import MatchWord
from . import ParameterInvaild
from . import OrderGen

#在候选词中选择关键词
ChooseWord = ChooseWord.ChooseWord

#匹配关键词
MatchWord = MatchWord.MatchWord

#参数校验
ParameterInvaild = ParameterInvaild.ParameterInvaild

#订单生成
OrderGen = OrderGen.OrderGen
