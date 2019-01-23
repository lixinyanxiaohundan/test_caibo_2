# -*- coding: utf-8 -*-
from com.caibo.ui.PublicPage import PublicPage

class HotAnchorPage(PublicPage):
    def __init__(self):
        pass

    resclass_hot_anchor="android.widget.TextView"
    restext_hot="热门"
    restext_follow="关注"
    
    #直播间
    #所有直播间id一样
    #顶呱呱直播间index:1
    #合买专场直播间index:2
    #vip财源滚滚直播间index:3
    #直播间id
    resid_anchor="com.dbljoy.lottery:id/anchor_cover"
    #房间名字id
    resid_room="com.dbljoy.lottery:id/room_name"
    #主播头像
    resid_head_icon="com.dbljoy.lottery:id/headIcon"
    #退出直播间按钮
    resid_exit_room="com.dbljoy.lottery:id/im_back"
    #拼单合买按钮
    resid_pindan_icon="com.dbljoy.lottery:id/fightalone"
    
    #直播间中聊天购买彩票购彩记录这几个模块没有id,,,使用className
    resclass_room="android.widget.TextView"
    #聊天模块
    restext_mess="聊天"
    #购买彩票模块
    restext_buy_lottery="购买彩票"
    #购彩记录模块
    restext_records="购彩记录"
    #聊天消息输入框
    resid_edit_mess="com.dbljoy.lottery:id/et_msg"
    #聊天消息发送按钮
    resid_send_mess="com.dbljoy.lottery:id/btn_sendmessage"
    #彩票购买按钮
    resid_buy_lottery="com.dbljoy.lottery:id/but_buy"
    #彩票详情
    resid_lottery_detail="com.dbljoy.lottery:id/details"
    #任意点击一次退出彩票详情  x256  y500
    resposition_lottery_detail_x=256
    resposition_lottery_detail_y=500
    #彩票张数:一张
    resid_one_lottery_num="com.dbljoy.lottery:id/bt_one"
    #3张
    resid_three_lottery_num="com.dbljoy.lottery:id/bt_Seven"
    #5张
    resid_five_lottery_num="com.dbljoy.lottery:id/bt_two"
    #10张
    resid_ten_lottery_num="com.dbljoy.lottery:id/bt_three"
    #整包
    resid_one_pack="com.dbljoy.lottery:id/bt_four"
    #刮票窗口
    #1号
    resid_one_window="com.dbljoy.lottery:id/oneWindow"
    #2号
    resid_two_window="com.dbljoy.lottery:id/towWindow"
    #3号
    resid_three_window="com.dbljoy.lottery:id/threeWindow"
    #4号
    resid_four_window="com.dbljoy.lottery:id/fourWindow"
    #确认购买
    resid_relbuy_button="com.dbljoy.lottery:id/but_buys"
    #关闭购彩页面
    resid_close_buy_button="com.dbljoy.lottery:id/barck"
    #查看刮票
    resid_view_lottery="com.dbljoy.lottery:id/but_pupo"
    #购彩记录下分类classname
    resclass_record="android.widget.TextView"
    #单买记录
    restext_buy_alone_record="单买记录"
    #拼单记录
    restext_collect_bills_record="拼单记录"
    #大奖待领
    restext_grand_prix_record="大奖待领"
    #单买记录classname  根据index查看,从0开始
    resclass_buy_alone_records="android.widget.RelativeLayout"
    
    
    
    #公告无id,此处根据绝对坐标点击
    resposition_notice_x1=241
    resposition_notice_y1=259
    resposition_notice_x2=400
    resposition_notice_y2=300
    