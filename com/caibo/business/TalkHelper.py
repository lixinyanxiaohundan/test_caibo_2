# -*- coding: utf-8 -*-
from test_caibo_2.com.caibo.api.Utils import Utils
from test_caibo_2.com.caibo.ui.MyInfoPage import MyInfoPage
from test_caibo_2.com.caibo.business.BaseHelper import BaseHelper
from test_caibo_2.com.caibo.ui.HotAnchorPage import HotAnchorPage
from test_caibo_2.com.caibo.business.HotAnchorHelper import HotAnchorHelper


class TalkHelper(BaseHelper):
    global driver

    def to_Hot_room(self):
        HotAnchorHelper.to_hot_page()
        HotAnchorHelper.to_anchor_room()
        Utils
