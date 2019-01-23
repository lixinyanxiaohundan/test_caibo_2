# -*- coding: utf-8 -*-
import time
import unittest
from com.caibo.api.Log import Log
from com.caibo.business.MyHelper import MyHelper


class Test_B_My(unittest.TestCase):
    
    def ___init___(self):
        print("aaa")
        pass
    #去我的页面  case_name保持10个字,不够了使用--填充  
    def test_my1(self):  
        case_name="点击进入我的页面--"
        log = Log()
        log.print_case_info_My(case_name)
        # 调用方法输入手机号,密码，用例名字，截图等待时间，是否初始化driver状态
        MyHelper.to_my_page(self,case_name, 3)  #点击我的
        time.sleep(2)
        print("本条用例执行通过")
          
        #清除缓存
    def test_my2(self):
        case_name="点击清除缓存"
        log = Log()
        log.print_case_info_My(case_name)
        # 调用方法输入手机号,密码，用例名字，截图等待时间，是否初始化driver状态
        MyHelper.clear_cache_cancel(self, case_name, 5)
        print("本条用例执行通过")