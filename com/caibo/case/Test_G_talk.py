# -*- coding: utf-8 -*-
import unittest
from test_caibo_2.com.caibo.api.Log import Log
from test_caibo_2.com.caibo.business.TalkHelper import TalkHelper
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

    # 输入空格并发送
    def test_talk1(self):
        case_name = "输入正确的内容"
        text = "略略略"
        Log.print_case_info_talk(case_name, text)
        TalkHelper.Talk_first(self, text, case_name, 1)
        print("%s 本次测试用例执行完成" %case_name)

    def test_talk2(self):
        case_name = "输入特殊符号"
        text = "@#$%_-+"
        Log.print_case_info_talk(case_name, text)
        TalkHelper.Talk(self, text, case_name, 1)
        print("%s 本次用例执行完成" %case_name)
        #

    def test_talk3(self):
        case_name = "输入数字"
        text = "1234567"
        Log.print_case_info_talk(case_name, text)
        TalkHelper.Talk(self, text, case_name, 1)
        print("%s本次用例执行完成" %case_name)

    def test_talk4(self):
        case_name = "输入英文"
        text = "hello world"
        Log.print_case_info_talk(case_name, text)
        TalkHelper.Talk(self, text, case_name, 1)
        print("%s 本次用例执行完成" % case_name)

    def test_talk5(self):
        case_name = "输入空格"
        text = "   "
        Log.print_case_info_talk(case_name, text)
        TalkHelper.Talk(self, text, case_name, 1)
        print("%s 本次用例执行完成" % case_name)

    def test_talk6(self):
        case_name = "输入表情"
        Log.print_case_info_talk(case_name)
        TalkHelper.Talkd(case_name, 1)
        pass
