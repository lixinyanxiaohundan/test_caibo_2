# -*- coding: utf-8 -*-
import unittest
from com.caibo.api.Log import Log
from com.caibo.business.MyInfoHelper import MyInfoHelper
from com.caibo.api.Utils import Utils


class Test_MyInfo(unittest.TestCase):
    
    def ___init___(self):
        print("aaa")
        pass
    
    #去我的个人信息页面  #case_name保持10个字,不够了使用--填充  
    def test_myinfo_a(self):  
        case_name="去我的个人信息页面-"
        Log.print_case_info_My(self,case_name)
        # 点击个人信息
        MyInfoHelper.to_my_info(self,case_name,2) 
        print("本条用例执行通过")
    #===========昵称模块用例=============
    #修改为已存在的昵称
    def test_myinfo_b(self):
        case_name="修改为已存在的昵称-"
        Log.print_case_info_My(self,case_name)
        # 点击个人信息
        MyInfoHelper.edit_nickname_error(self,"",case_name,0) 
        print("本条用例执行通过")
        
    #修改为1位的昵称(正常是2-16位)
    def test_myinfo_c(self):
        case_name="修改为1位的昵称--"
        Log.print_case_info_My(self,case_name)
        # 点击个人信息
        MyInfoHelper.edit_nickname_error(self,"n",case_name,0) 
        print("本条用例执行通过")
        
    #修改为17位的昵称(正常是2-16位)
    def test_myinfo_d(self):
        case_name="修改为17位的昵称-"
        Log.print_case_info_My(self,case_name)
        # 点击个人信息
        MyInfoHelper.edit_nickname_error(self,"零一二三四五六七八九一二三四五六七",case_name,0) 
        print("本条用例执行通过")
        
    #修改为特殊符号昵称(正常是2-16位)
    def test_myinfo_e(self):
        case_name="修改为特殊符号昵称-"
        Log.print_case_info_My(self,case_name)
        # 点击个人信息
        MyInfoHelper.edit_nickname_error(self,"...)(&^><?",case_name,0) 
        print("本条用例执行通过")
        
    #修改为正确格式的昵称(正常是2-16位)
    def test_myinfo_f(self):
        case_name="修改为正确格式昵称-"
        Log.print_case_info_My(self,case_name)
        MyInfoHelper.edit_nickname_right(self,Utils.creat_username(self),case_name,0) #使用随机数生成昵称避免重复(9位)
        print("本条用例执行通过")
    
    #===========实名认证信息模块用例=============
    #先实名认证才可以添加银行卡
    #身份证号和姓名都不输入点击提交
    def test_myinfo_g(self):
        case_name="都不输入点击提交--"
        rel_name=""
        rel_card=""
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 0)
        print("本条用例执行通过")
    
    #姓名输入一位,身份证号不填,点击提交
    def test_myinfo_h(self):
        case_name="姓名输入一位----"
        rel_name="n"
        rel_card=""
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 0)
        print("本条用例执行通过")
        
    #姓名输入七位,身份证号不填,点击提交
    def test_myinfo_i(self):
        case_name="姓名输入七位----"
        rel_name="adcdefg"
        rel_card=""
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 0)
        print("本条用例执行通过")
        
    #姓名输入四位,身份证号不填,点击提交
    def test_myinfo_j(self):
        case_name="姓名输入七位----"
        rel_name="adcdefg"
        rel_card=""
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 0)
        print("本条用例执行通过")
        
    #姓名输入特殊符号,身份证号不填,点击提交
    def test_myinfo_k(self):
        case_name="姓名输入特殊符号--"
        rel_name="---...///##" 
        rel_card=""
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 0)
        print("本条用例执行通过")
        
    #身份证号输入一位,姓名输入test,点击提交
    def test_myinfo_l(self):
        case_name="身份证号输入1位--"
        rel_name="test" 
        rel_card="1"
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 1)
        print("本条用例执行通过")
        
    #身份证号输入19位,姓名输入test,点击提交
    def test_myinfo_m(self):
        case_name="身份证号输入19位-"
        rel_name="test" 
        rel_card="1234567890123456789"
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 1)
        print("本条用例执行通过")
        
    #身份证号输入18个1,姓名输入test,点击提交
    def test_myinfo_n(self):
        case_name="身份证号输入18个1"
        rel_name="test" 
        rel_card="111111111111111111"
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 1)
        print("本条用例执行通过")
        
    #身份证号输入18位错误的,姓名输入test,点击提交
    def test_myinfo_o(self):
        case_name="身份证输入18位错误"
        rel_name="test" 
        rel_card="130424166658920218"
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 1)
        print("本条用例执行通过")
    
    #身份证号姓名输入正确的但是未满18岁的,点击提交------无测试数据
    def test_myinfo16(self):
        case_name="姓名输入特殊符号--"
        rel_name="test" 
        rel_card="130424166658920218"
        Log.print_case_info_identity(self, rel_name, rel_card, case_name)
        MyInfoHelper.identity_relname(self, rel_name, rel_card, case_name, 0)
        print("本条用例执行通过")   
         
    #个人信息-修改密码模块用例=============
    #修改密码--不输入手机号获取验证码
    def test_myinfo_p(self):
        case_name="不输入手机号点击获取"
        mobile=""
        Log.print_case_info_get_code(self, mobile, case_name)
        MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
        print("本条用例执行通过")
        
                
        #修改密码--输入1位手机号获取验证码
    def test_myinfo_q(self):
        case_name="输入1位点击获取--"
        mobile="1"
        Log.print_case_info_get_code(self, mobile, case_name)
        MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 0)
        print("本条用例执行通过")
        
        #修改密码--输入13位手机号获取验证码
    def test_myinfo_r(self):
        case_name="输入13位点击获取-"
        mobile="1234567890123"
        Log.print_case_info_get_code(self, mobile, case_name)
        MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
        print("本条用例执行通过")
              
                
        #修改密码--输入12位1获取验证码
    def test_myinfo_s(self):
        case_name="输入12个1点击获取"
        mobile="1111111111"
        Log.print_case_info_get_code(self, mobile, case_name)
        MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
        print("本条用例执行通过")
    
        #修改密码--输入特殊符号获取验证码
    def test_myinfo_t(self):
        case_name="输入特殊符号点击获取"
        mobile="***???//~~"
        Log.print_case_info_get_code(self, mobile, case_name)
        MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
        print("本条用例执行通过")
        
    #修改密码--输入正确但非本人手机号获取验证码
    def test_myinfo_u(self):
        case_name="输入正确但非本人号码"
        mobile="13683052819"
        Log.print_case_info_get_code(self, mobile, case_name)
        MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
        print("本条用例执行通过")
    
    #============个人信息-退出登录============    
    #退出登录点击取消
    def test_myinfo_v(self):
        case_name="退出登录点击取消--"
        print(case_name)
        MyInfoHelper.exit(self, 0, case_name, 1)
     
    #退出登录点击确定
    def test_myinfo_w(self):
        case_name="退出登录点击确认--"
        print(case_name)
        MyInfoHelper.exit(self, 1, case_name, 1)

#         
#             #修改密码--不输入手机号获取验证码
#     def test_myinfo_x(self):
#         case_name="不输入手机号点击获取"
#         mobile=""
#         Log.print_case_info_get_code(self, mobile, case_name)
#         MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
#         print("本条用例执行通过")
#         
#             #修改密码--不输入手机号获取验证码
#     def test_myinfo_y(self):
#         case_name="不输入手机号点击获取"
#         mobile=""
#         Log.print_case_info_get_code(self, mobile, case_name)
#         MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
#         print("本条用例执行通过")
#         
#             #修改密码--不输入手机号获取验证码
#     def test_myinfo_z(self):
#         case_name="不输入手机号点击获取"
#         mobile=""
#         Log.print_case_info_get_code(self, mobile, case_name)
#         MyInfoHelper.get_code_by_mobile(self, mobile, case_name, 1)
#         print("本条用例执行通过")
#         