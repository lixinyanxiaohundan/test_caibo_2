# -*- coding: utf-8 -*-
import time
import unittest
from com.caibo.api.Log import Log
from com.caibo.business.MyHelper import MyHelper


class Test_C_My(unittest.TestCase):
    
    def ___init___(self):
        print("aaa")
        pass
    
    
    #去我的页面 #case_name保持10个字,不够了使用--填充  
    def test_my_a(self):  
        case_name="点击进入我的页面--"
        log = Log()
        log.print_case_info_My(case_name)
        # 调用方法输入手机号,密码，用例名字，截图等待时间，是否初始化driver状态
        MyHelper.to_my_page(self,case_name, 3)  #点击我的
        time.sleep(2)
         
    #==============充值功能测试用例============
    #一般跳转到微信登录页面即充值功能正常使用
    #充值10元
    def test_my_b(self):  
        case_name="充值10元-----"
        log = Log()
        log.print_case_info_My(case_name)
        MyHelper.recharge_wechat_click_first(self, 10, case_name, 2)
        time.sleep(2)
        
    def test_my_c(self):  
        case_name="充值15元-----"
        log = Log()
        log.print_case_info_My(case_name)
        MyHelper.recharge_wechat_click(self, 15, case_name, 2)
        time.sleep(2)

    #清除缓存---取消
    def test_my_o(self):
        case_name="点击清除缓存取消--"
        log = Log()
        log.print_case_info_My(case_name)
        MyHelper.clear_cache_cancel(self, case_name, 5)
        
    #清除缓存---确定
    def test_my_z(self):
        case_name="点击清除缓存确定--"
        log = Log()
        log.print_case_info_My(case_name)
        MyHelper.clear_cache_really(self, case_name, 5)
