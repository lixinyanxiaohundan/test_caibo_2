# -*- coding: utf-8 -*-
from test_caibo_2.com.caibo.api.Utils import Utils
from test_caibo_2.com.caibo.ui.MyInfoPage import MyInfoPage
from test_caibo_2.com.caibo.business.BaseHelper import BaseHelper
from test_caibo_2.com.caibo.ui.HotAnchorPage import HotAnchorPage

class HotAnchorHelper(BaseHelper):
    global driver

    def __init__(self):   
        pass
   
    #去热门主播页面
    def to_hot_page(self,case_name,second=0):
        try:
            hot_anchor_page = HotAnchorPage()
            util=Utils()
            util.getElementById(HotAnchorHelper.driver,hot_anchor_page.resid_home_button).click()
            if second > 0:
                #util.take_screenShot(LoginHelper.driver, case_name, second)
                util.getImage(HotAnchorHelper.driver, case_name, second)
            else:
                #util.take_screenShot(LoginHelper.driver, case_name, 0)
                util.getImage(HotAnchorHelper.driver, case_name, 0)
            print("本次测试完成")
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
    
    #进入id为anchor_index的直播间
    def to_anchor_room(self,case_name,anchor_index,second=0):
        try:
            hot_anchor_page = HotAnchorPage()
            util=Utils()
            util.get_element_by_index(HotAnchorHelper.driver, hot_anchor_page.resid_anchor, anchor_index).click()
            if second > 0:
                #util.take_screenShot(LoginHelper.driver, case_name, second)
                util.getImage(HotAnchorHelper.driver, case_name, second)
            else:
                #util.take_screenShot(LoginHelper.driver, case_name, 0)
                util.getImage(HotAnchorHelper.driver, case_name, 0)
            print("本次测试完成")
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError

    def exit_room(self):
        try:
            # HotAnchorHelper.to_hot_page()
            # HotAnchorHelper.to_anchor_room()
            self.driver.keyevent(4)  # 方法一 手机物理键

            hot_anchor_page = HotAnchorPage()
            Utils.getElementById().click()  # 方法二 直播间右上方退出按钮，为保万一最好点击两次=。=
            pass
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError

