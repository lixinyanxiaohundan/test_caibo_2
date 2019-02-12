# -*- coding: utf-8 -*-
class Log:
    
    def print_case_info_Login(self,mobile,pwd,mes):
        print('执行登录相关测试用例：\n'+mes+'\n参数：\n'+'mobile:'+mobile+'\n'+'pwd:'+pwd)
        pass
    def print_case_info_My(self,mes):
        print("执行测试用例：\n"+mes)
        pass
    def print_case_info_identity(self,rel_name,rel_card,mes):
        print('执行实名认证相关测试用例：\n'+mes+'\n参数：\n'+'name:'+rel_name+'\n'+'card:'+rel_card)
        pass
    
    def print_case_info_get_code(self,mobile,case_name):
        print('执行根据手机号获取验证码相关测试用例：\n'+case_name+'\n参数：\n'+'mobile:'+mobile)
        pass
        
    def print_case_info_recharge(self,amount,case_name):
        print('执行充值相关测试用例：\n'+case_name+'\n参数：\n'+'金额:'+amount)
        pass

    def print_case_info_talk(self, case_name, cont):
        print('执行直播间内聊天的测试用例：\n'+case_name + '\n参数：\n'+'cont' + cont)
        pass