'''
Created on 2018年12月19日

@author: lipengjie
'''
from com.caibo.ui.PublicPage import PublicPage
from com.caibo.ui.MyPage import MyPage

class FinancialOperationPage(MyPage):   #财务操作页面,包含充值和提现等
    '''
    classdocs
    '''


    def __init__(self):
    
        pass
    
    resid_recharge_ten = "com.dbljoy.lottery:id/btn_one"   #充值10元
    resid_recharge_twenty = "com.dbljoy.lottery:id/btn_two"   #充值20
    resid_recharge_fifty = "com.dbljoy.lottery:id/btn_three"   #充值50
    resid_recharge_oneHundred = "com.dbljoy.lottery:id/btn_four"   #充值 100
    resid_recharge_oneHundredAndFifty = "com.dbljoy.lottery:id/btn_five"   #充值150
    resid_recharge_twoHundred = "com.dbljoy.lottery:id/btn_six"   #充值200
    resid_recharge_threeHundred = "com.dbljoy.lottery:id/btn_seven"   #充值300
    resid_recharge_fiveHundred = "com.dbljoy.lottery:id/btn_eight"   #充值500
    resid_recharge_financial_rocord = "com.dbljoy.lottery:id/text_history"   #充值记录
    resid_recharge_wechatpay = "com.dbljoy.lottery:id/re_wechatpay"   #微信支付
    resid_recharge_unionpay = "com.dbljoy.lottery:id/re_unionpay"   #银联支付
    resid_recharge_money_input = "com.dbljoy.lottery:id/edit_money"   #充值金额输入框
    resid_recharge_commit = "com.dbljoy.lottery:id/btn_recharge"   #确认充值按钮
    resid_recharge_wechat_back = "com.tencent.mm:id/jc"   #微信充值页返回按钮
    resid_recharge_complete_x1 = 828   #充值成功后的完成按钮坐标
    resid_recharge_complete_y1 = 901
    resid_recharge_complete_x2 = 445
    resid_recharge_complete_y2 = 942
    resposition_recharge_instruction_disagree_x1 = 137   #第一次进入充值,充值说明的不同意按钮坐标
    resposition_recharge_instruction_disagree_y1 = 1010 
    resposition_recharge_instruction_disagree_x2 = 275
    resposition_recharge_instruction_disagree_y2 = 1084 
    resposition_recharge_instruction_agree_x1 = 469   #第一次进入充值,充值说明的同意按钮坐标
    resposition_recharge_instruction_agree_y1 = 1034 
    resposition_recharge_instruction_agree_x2 = 574
    resposition_recharge_instruction_agree_y2 = 1079 
    
    
    