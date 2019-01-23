# -*- coding: utf-8 -*-
from com.caibo.api.Utils import Utils
from com.caibo.ui.MyInfoPage import MyInfoPage
from com.caibo.business.BaseHelper import BaseHelper
from com.caibo.ui.MyPage import MyPage

class CashWithDrawalHelper(BaseHelper):   #财务记录
    global driver

    def __init__(self):   
        pass
   


    def to_cash_with_drawl(self,case_name):
        try:
            util=Utils()
            util.getElementById(CashWithDrawalHelper.driver,MyPage.resid_my_button).click()
            util.getElementById(CashWithDrawalHelper.driver,MyPage.resid_my_record).click()
            util.take_screenShot(CashWithDrawalHelper.driver, case_name, 2)
            util.getElementById(CashWithDrawalHelper.driver,MyPage.resid_back_button).click()
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError