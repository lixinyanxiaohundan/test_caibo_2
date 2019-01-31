# -*- coding: utf-8 -*-
from test_caibo_2.com.caibo.business.LoginHelper import LoginHelper
from test_caibo_2.com.caibo.api.Log import Log
import unittest
import pytest
import time


class Test_a_l(pytest):
    pass


class Test_A_Login(unittest.TestCase):    

    # case_name保持10个字,不够了使用__填充
    # 每天要把HTMLTestRunner中第722行的文件夹名字改为当天的,要不无法查看报告中的图片
    # 第一个测试方法需要初始化状态,driver为1进行初始化
    # 只输入错误账号（11111111111）点击登录
    def test_login1(self):
        mobile="11111111111"
        pwd=""
        case_name="输入错误账号登录-1"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,0,1)  # 调用方法输入手机号,密码，用例名字
        print("执行结束")
    # 只输入错误手机号（1503107628）10位点击登录
    def test_login2(self):
        mobile="1503107628"
        pwd=""
        case_name="输入错误账号登录-2"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,0,0)  # 调用方法输入手机号,密码，用例名字
        print("执行结束")
    # 只输入错误手机号（150310762800）12位点击登录
    def test_login3(self):
        mobile="150310762832"
        pwd=""
        case_name="输入错误账号登录-3"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,0,0)  # 调用方法输入手机号,密码，用例名字
        print("执行结束")
    # 只输入错误手机号（****————？？）特殊符号点击登录
    def test_login4(self):
        mobile="****————？？"
        pwd=""
        case_name="输入特殊符号登录-4"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,0,0)  # 调用方法输入手机号,密码，用例名字
        print("执行结束")
    # 只输入不存在的手机号（15031028965）点击登录
    def test_login5(self):
        mobile="15128222629"
        pwd=""
        case_name="输入不存在的账号-5"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,0,0)  # 调用方法输入手机号,密码，用例名字
        print("执行结束")
    # 只输入正确手机号（13683052815）错误密码（123456789）点击登录

    def test_login6(self):
        mobile="15830921770"
        pwd="23345667"
        case_name="正确账号错误密码-6"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,1,0)  # 调用方法输入手机号,密码，用例名字
        print("执行结束")
    # 只输入正确手机号（13683052815）点击登录
    def test_login7(self):
        mobile="15830921770"
        pwd=""
        case_name="正确账号不填密码-7"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,0,0)  # 调用方法输入手机号,密码，用例名字
        print("执行结束")

    # 账号密码输入正确点击登陆
    def test_login8(self):  
        mobile="15830921770"
        pwd="111111"
        case_name="输入正确账号密码-8"
        Log.print_case_info_Login(self,mobile,pwd,case_name)
        LoginHelper.login(self,mobile,pwd,case_name,5,0)  # 调用方法输入手机号,密码，用例名字
        time.sleep(2) 
     

