# -*- coding: utf-8 -*-
from test_caibo_2.com.caibo.ui.PublicPage import PublicPage

class MyInfoPage(PublicPage):   #个人信息页面
    def __init__(self):
        pass
    #头像
    #最外层头像    
    resid_headportrait_button="com.dbljoy.lottery:id/head_portrait"
    #myinfo层头像按钮
    resid_rel_headportrait_button = "com.dbljoy.lottery:id/re_headprotait"
    #头像页右上角更换头像按钮
    resid_set_headportrait_button = "com.dbljoy.lottery:id/img_menu"
    #红米从手机相册选择按钮坐标位置:x1 200 y1 1000  x2 497  y2 1046
    resposition_selectphoto_redmi_x1=200
    resposition_selectphoto_redmi_y1=1000
    resposition_selectphoto_redmi_x2=497
    resposition_selectphoto_redmi_y2=1046
    #红米拍照按钮坐标位置:x1 272 y1 1097 x2 437 y2 1159
    resid_myinfo_button="com.dbljoy.lottery:id/entrance"  #个人信息按钮  
    resid_myinfo_hedaportrait = "com.dbljoy.lottery:id/re_headprotait"  #个人信息-头像
    resid_myinfo_nickname = "com.dbljoy.lottery:id/re_nickname"  #个人信息-昵称
    
    resid_nickname_input = 'com.dbljoy.lottery:id/text_name'  #昵称输入框
    
    resid_savename_button = "com.dbljoy.lottery:id/btn_save_name"  #保存昵称按钮
    resid_mes_button = "android:id/button2"  #提示消息框的确认按钮
    resid_myinfo_bankcard = "com.dbljoy.lottery:id/re_card"  #个人信息-银行卡
   
    resid_myinfo_relname = "com.dbljoy.lottery:id/text_isrealname"  #个人信息-实名信息   已实名用户此栏不可点击,,注意!!!!  弄个连接数据库的,一键清除数据 初始化数据,为测试做准备
    resid_myinfo_identity = "com.dbljoy.lottery:id/re_identity"  #个人信息-实名信息 未认证
    resid_identity_relname = "com.dbljoy.lottery:id/edit_name"   #实名认证-姓名
    resid_identity_relcard = "com.dbljoy.lottery:id/edit_card"   #实名认证-身份证号
    resid_identity_commit_button = "com.dbljoy.lottery:id/btn_commit"   #提交认证信息按钮
    
    resid_myinfo_edit_mobile = "com.dbljoy.lottery:id/re_phone"    #个人信息-绑定手机号    绑定手机号不可点击

    resid_myinfo_updatepwd = "com.dbljoy.lottery:id/re_changepwd"   #个人信息-修改密码
    resid_updatepwd_mobile = "com.dbljoy.lottery:id/edit_phone"   #修改密码-手机号
    resid_updatepwd_code = "com.dbljoy.lottery:id/edit_securitycode"   #修改密码-验证码
    resid_updatepwd_get_code_button = "com.dbljoy.lottery:id/btn_time"   #修改密码-获取验证码按钮
    resid_updatepwd_pwd = "com.dbljoy.lottery:id/edit_pwd"    #修改密码-第一遍密码
    resid_updatepwd_relpwd = "com.dbljoy.lottery:id/edit_re_pwd"   #修改密码-第二遍密码
    resid_updatepwd_commit_button = "com.dbljoy.lottery:id/btn_save_pwd"   #修改密码-提交按钮    
    
    resid_myinfo_exit_button = "com.dbljoy.lottery:id/text_exitlogin"   #退出登录按钮
     
    resposition_cancel_x1 = 133   # 133 691 249 744 取消按钮
    resposition_cancel_y1 = 691
    resposition_cancel_x2 = 249
    resposition_cancel_y2 = 744
    resposition_confirm_x1 = 462   #462 695 576  741 确认按钮
    resposition_confirm_y1 = 695
    resposition_confirm_x2 = 576
    resposition_confirm_y2 = 741
    
    resid_my_button = "com.dbljoy.lottery:id/my"  #我的页面按钮


        