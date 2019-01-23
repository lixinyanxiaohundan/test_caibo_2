# -*- coding: utf-8 -*-
import unittest
from com.caibo.api.Log import Log
from com.caibo.business.HotAnchorHelper import HotAnchorHelper

#财务记录
class Test_HotAnchor(unittest.TestCase):
    
    #直播间
    #所有直播间id一样
    #顶呱呱直播间index:4
    #合买专场直播间index:10
    #vip财源滚滚直播间index:9
    def ___init___(self):
        print("aaa")
        pass
    #case_name保持10个字,不够了使用--填充  
    #点击进入热门主播页
    def test_hotAnchor1(self):  
        case_name="点击进入热门主播页-"
        Log.print_case_info_My(self,case_name)
        # 调用方法输入手机号,密码，用例名字，截图等待时间，是否初始化driver状态
        HotAnchorHelper.to_hot_page(self, case_name)#点击我的
        print("本条用例执行通过")
         
    #点击进入顶呱呱直播间
    def test_hotAnchor2(self):  
        case_name="点击进入顶呱呱直播间"
        Log.print_case_info_My(self,case_name)
        # 调用方法输入用例名字,直播间索引,从0开始,0是第一个直播间
        HotAnchorHelper.to_anchor_room(self,case_name,0,2)
        print("本条用例执行通过")