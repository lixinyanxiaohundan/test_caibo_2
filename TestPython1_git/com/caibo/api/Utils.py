# -*- coding: utf-8 -*-
import datetime
import time
import os
import subprocess
import random
class Utils:
    def __init__(self):
        pass
        #getElementById(driver,loginPage.mobile)
        #return driver3.findElementById(mobile);
            
    #根据元素id获取元素
    def getElementById(self,driver3,resid):
        return driver3.find_element_by_id(resid)
        #return driver3.findElementById(mobile);
        
    #根据传来的id获取其中索引为anchor_index的元素
    def get_element_by_index(self,driver3,resid,anchor_index):
        return driver3.find_elements_by_id(resid)[anchor_index]
        #return eles.index(3)
            
    #获取当前的日期并转换格式    
    def getDateTime(self):
        now_time = datetime.datetime.now().strftime('%Y_%m_%d')
        return now_time;
   
    #点击屏幕坐标框,两个参数一个是左上角xy坐标,一个是右下角xy坐标
    def tap(self,driver,x,y,x1,y1):
        #取消  128  680,245-744
        #确定  449  695,600 746
        time.sleep(2)
        driver.tap([(x,y), (x1,y1)], 5) 
    
    #使用adb命令点击指定坐标,x,y
    def adb_click(self,x,y):
        time.sleep(2)
        order='adb devices' #创建命令
        pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
        
        
    def mkdir(self,path):
        # 去除首位空格
        path=path.strip()
        # 去除尾部 \ 符号
        path=path.rstrip("\\")
     
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
     
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path) 
     
            print ('%s 创建成功'%path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print ('%s 目录已存在'%path)
            return False
        
    
    def getImage(self,driver,name="takeShot",second=0):
        '''
        截取图片,并保存在screenShots文件夹
        :return: 无
        '''
        time.sleep(second)
        type = '.png'
        day = time.strftime("%Y_%m_%d",time.localtime(time.time()))
        temp_fq = '../screenShots/'+day
        now_date_time=Utils.getDateTime(self)
        fq=temp_fq+'/'+now_date_time+name+type
        imgPath = fq
        driver.get_screenshot_as_file(imgPath)
        print  (u'screenShots',now_date_time+name,'.png')
    
    def creat_username(self):
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        d=random.randint(1,10)
        e=random.randint(1,10)
        f=random.randint(1,10)
        g=random.randint(1,10)
        h=random.randint(1,10)
        i=random.randint(1,10)
        str_a=str(a)
        str_b=str(b)
        str_c=str(c)
        str_d=str(d)
        str_e=str(e)
        str_f=str(f)
        str_g=str(g)
        str_h=str(h)
        str_i=str(i)
        
        str_number=str_a+str_b+str_c+str(c)+str_d+str_e+str_f+str_g+str_h+str_i
        return str_number
    #name 截图的名称 secon 等待几秒截图
    def take_screenShot(self,driver,name="takeShot",second=0):
        '''
        method explain:获取当前屏幕的截图
        parameter explain：【name】 截图的名称
        Usage:
            device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
        '''
        time.sleep(second)
        day = time.strftime("%Y_%m_%d",time.localtime(time.time()))
        fq = "../screenShots/"+day  
        #fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
        now_date_time=Utils.getDateTime(self)
        type = '.png'
        filename = ""
        if os.path.exists(fq):
            filename = fq+"/"+now_date_time+"_"+name+type
        else:
            os.makedirs(fq)
            filename = fq+"/"+now_date_time+"_"+name+type
        driver.get_screenshot_as_file(filename)
        