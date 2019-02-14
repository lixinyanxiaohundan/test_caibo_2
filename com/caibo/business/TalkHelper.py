# -*- coding: utf-8 -*-
from test_caibo_2.com.caibo.api.Utils import Utils
from test_caibo_2.com.caibo.ui.MyInfoPage import MyInfoPage
from test_caibo_2.com.caibo.business.BaseHelper import BaseHelper
from test_caibo_2.com.caibo.ui.HotAnchorPage import HotAnchorPage
from test_caibo_2.com.caibo.business.HotAnchorHelper import HotAnchorHelper


class TalkHelper(BaseHelper):
    global driver

    def Talk(self, content,case_name):
        # 点击聊天，默认在聊天模块
        Utils.get_element_by_text(HotAnchorPage.restext_mess).click()
        # 点击输入框并输入，发送
        Utils.getElementById(HotAnchorPage.resid_edit_mess).send_keys(content)
        Utils.getElementById(HotAnchorPage.resid_send_mess).click()
