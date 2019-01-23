# -*- coding: utf-8 -*-
from com.caibo.api.Utils import Utils
from com.caibo.ui.MyInfoPage import MyInfoPage
from com.caibo.business.BaseHelper import BaseHelper
from com.caibo.ui.HotAnchorPage import HotAnchorPage

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
