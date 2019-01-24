# -*- coding: utf-8 -*-
from test_caibo_2.com.caibo.api.Utils import Utils
from test_caibo_2.com.caibo.ui.LoginPage import LoginPage
from test_caibo_2.com.caibo.business.BaseHelper import BaseHelper

class LoginHelper(BaseHelper):
    global driver

    def __init__(self):   
        pass
   
    # 手机号，密码，用例标题，秒数，driver的状态（1就进行第一次初始化，0就代表已初始化）
    # 手机号密码为空则不输入
    def login(self, mobile, pwd, case_name, second, driver_stat):
        try:
    
            if driver_stat==1:
                print("driver_stat=1,初始化driver")
                LoginHelper.driver = BaseHelper.get_redmi_driver(self)  # 创建driver
            else:
                
                pass
            loginPage = LoginPage()
            util=Utils()
            if mobile == "":
                util.getElementById(LoginHelper.driver, loginPage.mobile).click()
                util.getElementById(LoginHelper.driver, loginPage.mobile).clear()
            else:
                util.getElementById(LoginHelper.driver, loginPage.mobile).click()
                util.getElementById(LoginHelper.driver, loginPage.mobile).clear()
                util.getElementById(LoginHelper.driver, loginPage.mobile).send_keys(mobile)
            if pwd == "":
                util.getElementById(LoginHelper.driver, loginPage.password).click()
                util.getElementById(LoginHelper.driver, loginPage.password).clear()
            else:
                util.getElementById(LoginHelper.driver, loginPage.password).click()
                util.getElementById(LoginHelper.driver, loginPage.password).clear()
                util.getElementById(LoginHelper.driver, loginPage.password).send_keys(pwd)
            util.getElementById(LoginHelper.driver, loginPage.seepwd).click()
            # util.clearText(loginPage.password, driver);
            # util.clearText(driver, loginPage.password);
            LoginHelper.driver.hide_keyboard()
            util.getElementById(LoginHelper.driver, loginPage.loginButton).click()
            if second > 0:
                #util.take_screenShot(LoginHelper.driver, case_name, second)
                util.getImage(LoginHelper.driver, case_name, second)
            else:
                #util.take_screenShot(LoginHelper.driver, case_name, 0)
                util.getImage(LoginHelper.driver, case_name, 0)
            print("本次测试完成")
        
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError

