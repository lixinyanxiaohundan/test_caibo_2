# -*- coding: utf-8 -*-
from test_caibo_2.com.caibo.api.Utils import Utils
from test_caibo_2.com.caibo.business.BaseHelper import BaseHelper
from test_caibo_2.com.caibo.ui.HotAnchorPage import HotAnchorPage
from test_caibo_2.com.caibo.business.HotAnchorHelper import HotAnchorHelper


class TalkHelper(BaseHelper):
    global driver

    def Talk_first(self, text, case_name, second):
        try:
            # 点击聊天(默认在聊天模块)
            Utils.get_element_by_text(HotAnchorPage.restext_mess).click()
            # 点击输入框并输入，发送
            Utils.getElementById(HotAnchorPage.resid_edit_mess).send_keys(text)
            Utils.getElementById(HotAnchorPage.resid_send_mess).click()
            if second > 0:
                # util.take_screenShot(LoginHelper.driver, case_name, second)
                Utils.getImage(HotAnchorHelper.driver, case_name, second)
            else:
                # util.take_screenShot(LoginHelper.driver, case_name, 0)
                Utils.getImage(HotAnchorHelper.driver, case_name, 0)
            print("本次测试完成")
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError

    def Talk(self, text, case_name, second):
        try:
            # 点击输入框并输入，发送
            Utils.getElementById(HotAnchorPage.resid_edit_mess).send_keys(text)
            Utils.getElementById(HotAnchorPage.resid_send_mess).click()
            if second > 0:
                # util.take_screenShot(LoginHelper.driver, case_name, second)
                Utils.getImage(HotAnchorHelper.driver, case_name, second)
            else:
                # util.take_screenShot(LoginHelper.driver, case_name, 0)
                Utils.getImage(HotAnchorHelper.driver, case_name, 0)
            print("本次测试完成")
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError

    # 表情
    def Talkd(self, case_name, second):
        try:
            Utils.getElementById(HotAnchorPage.resid_edit_mess).click()
            # 点击表情，选择一个表情扔出去!，发送
            # 坐标点击表情呀~~~

            Utils.getElementById(HotAnchorPage.resid_send_mess).click()
            if second > 0:
                # util.take_screenShot(LoginHelper.driver, case_name, second)
                Utils.getImage(HotAnchorHelper.driver, case_name, second)
            else:
                # util.take_screenShot(LoginHelper.driver, case_name, 0)
                Utils.getImage(HotAnchorHelper.driver, case_name, 0)
            print("本次测试完成")
        except Exception as e:
            print("发现异常")
            print(e)
            raise SystemError
