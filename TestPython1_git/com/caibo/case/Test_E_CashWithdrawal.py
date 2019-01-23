# -*- coding: utf-8 -*-
import unittest
from com.caibo.api.Log import Log
from com.caibo.business.CashWithDrawalHelper import CashWithDrawalHelper

#财务记录
class Test_MyInfo(unittest.TestCase):
    def ___init___(self):
        print("aaa")
        pass
    
    #点击进入财务记录
    def test_myinfo1(self):  
        case_name="点击进入财务记录"
        log = Log()
        log.print_case_info_My(case_name)
        # 调用方法输入手机号,密码，用例名字，截图等待时间，是否初始化driver状态
        CashWithDrawalHelper.to_cash_with_drawl(self, case_name)
        print("本条用例执行通过")