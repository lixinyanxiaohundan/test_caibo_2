# -*- coding: utf-8 -*-
import unittest
from test_caibo_2.com.caibo.api.Log import Log
from test_caibo_2.com.caibo.business.HotAnchorHelper import HotAnchorHelper
from test_caibo_2.com.caibo.api.Utils import Utils


# 财务记录
class Test_Talk(unittest.TestCase):
    
    # 直播间
    # 所有直播间id一样
    # 顶呱呱直播间index:4
    # 合买专场直播间index:10
    # vip财源滚滚直播间index:9
    def ___init___(self):
        print("aaa")
        pass

    # case_name保持10个字,不够了使用--填充
    #
    def test_talk1(self):
        case_name = "输入空格并发送"
        Log.print_case_info_talk(case_name, )
        pass
