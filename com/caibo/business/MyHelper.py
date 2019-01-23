# -*- coding: utf-8 -*-
from com.caibo.api.Utils import Utils
from com.caibo.ui.MyPage import MyPage
from com.caibo.business.BaseHelper import BaseHelper
import time
from com.caibo.ui.FinancialRecords import Financialecords
from com.caibo.ui.FinancialOperationPage import FinancialOperationPage

class MyHelper(BaseHelper):
    global driver
    def __init__(self):
        pass
   
    # 手机号，密码，用例标题，秒数，driver的状态（1就进行第一次初始化，0就代表已初始化）
    # 手机号密码为空则不输入
    def to_my_page(self,case_name,second):
        try:
            time.sleep(second)
            my_page = MyPage()
            util=Utils()
            util.getElementById(MyHelper.driver,my_page.resid_my_button).click()
            if second>0 :
                util.getImage(MyHelper.driver, case_name, second)
            else:
                util.getImage(MyHelper.driver, case_name, second)
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
        
    def recharge_wechat_click(self,amount,case_name,second):   #点击金额进行充值
        try:
            time.sleep(second)
            Utils.getElementById(self,MyHelper.driver,MyPage.resid_my_button).click()
            Utils.getElementById(self,MyHelper.driver,MyPage.resid_recharge).click()
            if(amount==10):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_ten).click()
                
            elif(amount==20):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_twenty).click()
                
            elif(amount==50):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_fifty).click()
            elif(amount==100):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_oneHundred).click()
            elif(amount==150):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_oneHundredAndFifty).click()
            elif(amount==200):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_twoHundred).click()
            elif(amount==300):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_threeHundred).click()
            elif(amount==500):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_fiveHundred).click()
            else:
                print("请输入要点击选择的正确金额")
                raise SystemError
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_wechatpay).click()
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_commit).click()
            if second>0 :
                Utils.getImage(self,MyHelper.driver, case_name, second)
            else:
                Utils.getImage(self,MyHelper.driver, case_name, 1)
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_wechat_back).click()
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_back_button).click()
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
        
    def recharge_wechat_click_first(self,amount,case_name,second):   #点击金额进行充值
        try:
            time.sleep(second)
            Utils.getElementById(self,MyHelper.driver,MyPage.resid_my_button).click()
            Utils.getElementById(self,MyHelper.driver,MyPage.resid_recharge).click()
            if(amount==10):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_ten).click()
                
            elif(amount==20):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_twenty).click()
                
            elif(amount==50):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_fifty).click()
            elif(amount==100):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_oneHundred).click()
            elif(amount==150):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_oneHundredAndFifty).click()
            elif(amount==200):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_twoHundred).click()
            elif(amount==300):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_threeHundred).click()
            elif(amount==500):
                Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_fiveHundred).click()
            else:
                print("请输入要点击选择的正确金额")
                raise SystemError
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_wechatpay).click()
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_commit).click()
            Utils.tap(self,MyHelper.driver,FinancialOperationPage.resposition_recharge_instruction_agree_x1,
                      FinancialOperationPage.resposition_recharge_instruction_agree_y1,
                      FinancialOperationPage.resposition_recharge_instruction_agree_x2,
                      FinancialOperationPage.resposition_recharge_instruction_agree_y2)
            if second>0 :
                Utils.getImage(self,MyHelper.driver, case_name, second)
            else:
                Utils.getImage(self,MyHelper.driver, case_name, 1)
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_recharge_wechat_back).click()
            Utils.getElementById(self,MyHelper.driver,FinancialOperationPage.resid_back_button).click()
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
    
    def recharge_wechat_input(self,amount,case_name,second):    #输入金额进行充值
        try:
            time.sleep(second)
            Utils.getElementById(self,MyHelper.driver,MyPage.resid_my_button).click()
            
            if second>0 :
                Utils.getImage(self,MyHelper.driver, case_name, second)
            else:
                Utils.getImage(self,MyHelper.driver, case_name, 1)
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError

    def to_exhibition_room(self,case_name,second):
        try:
            time.sleep(second)
            my_page = MyPage()
            util=Utils()
            util.getElementById(MyHelper.driver,my_page.resid_exhibitionRoom_button).click();
            print("点击大奖展厅完成")
            if second>0 :
                util.take_screenShot(MyHelper.driver,case_name,second)
            else:
                util.take_screenShot(MyHelper.driver,case_name,0)
        
            pass
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
    
    def clear_cache_cancel(self,case_name,second):   #清理缓存点取消
        try:
            time.sleep(second)
            my_page = MyPage()
            util=Utils()
            util.getElementById(MyHelper.driver,my_page.resid_my_button)
            #点击清理缓存,会弹出确认框
            util.getElementById(MyHelper.driver,my_page.resid_clear_cache).click()
            #由于uiauto定位不到确认框元素,此处采用绝对定位
            #取消  128  680,245-744
            #确定  449  695,600 746
            #点击取消
            time.sleep(2)
            util.tap(MyHelper.driver, 128, 680, 245, 744)
            if second>0 :
                util.take_screenShot(MyHelper.driver,case_name,second)
            else:
                util.take_screenShot(MyHelper.driver,case_name,0)
        except Exception as e:
            print("发现异常")
            print(e)
            Utils.getElementById(self, MyHelper.driver, MyPage.resid_back_button)
            raise SystemError
        
    def clear_cache_really(self,case_name,second):   #清理缓存点确定
        try:
            time.sleep(second)
            my_page = MyPage()
            util=Utils()
            util.getElementById(MyHelper.driver,my_page.resid_my_button)
            #点击清理缓存,会弹出确认框
            util.getElementById(MyHelper.driver,my_page.resid_clear_cache).click()
            #由于uiauto定位不到确认框元素,此处采用绝对定位
            #取消  128  680,245-744
            #确定  449  695,600 746
            #点击取消
            util.tap(MyHelper.driver, 449, 695, 600, 746)
            if second>0 :
                util.take_screenShot(MyHelper.driver,case_name,second)
            else:
                util.take_screenShot(MyHelper.driver,case_name,0)
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
        
        
