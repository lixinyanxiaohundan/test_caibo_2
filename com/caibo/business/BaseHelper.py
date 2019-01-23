# -*- coding: utf-8 -*-
import os, time, unittest
from com.caibo.api.Utils import Utils
from appium import webdriver


class BaseHelper:
    global driver

    def __init__(self):
        print("baseHelper初始化")
        
    #初始化红米    
    def get_redmi_driver(self):
        PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))  # 不写这一句也OK
        # 红米
        redmi_device_name="bc43cf2"  #设备名
        red_andorid_version="7.1.2"  #安卓版本

        # oppo  a 57
        # oppoDeviceName="4f712500"  # 设备名
        # oppoAndoridVersion="6.0.1"  # 安卓版本

        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        #desired_caps['platformVersion'] = red_andorid_version  # 设备系统版本
        #desired_caps['deviceName'] = redmi_device_name  # 设备名称
        desired_caps['platformVersion'] = "7.1.2"  # 设备系统版本
        desired_caps['deviceName'] = "bc43cf2"  # 设备名称
        desired_caps['appPackage'] = 'com.dbljoy.lottery' 
        desired_caps['appActivity'] = '.ui.activities.TransitionActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        BaseHelper.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        print("设备初始化成功")
        time.sleep(5)
        return BaseHelper.driver
    #初始化oppo
    def get_oppo_driver(self):
        oppo_device_name="a6e29c44"   #设备名
        oppo_android_verison="5.1.1"   #安卓版本
        # oppo  a 57
        # oppoDeviceName="4f712500"  # 设备名
        # oppoAndoridVersion="6.0.1"  # 安卓版本

        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        #desired_caps['platformVersion'] = red_andorid_version  # 设备系统版本
        #desired_caps['deviceName'] = redmi_device_name  # 设备名称
        desired_caps['platformVersion'] = oppo_android_verison  # 设备系统版本
        desired_caps['deviceName'] = oppo_device_name  # 设备名称
        desired_caps['appPackage'] = 'com.dbljoy.lottery' 
        desired_caps['appActivity'] = '.ui.activities.TransitionActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        BaseHelper.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        print("设备初始化成功")
        time.sleep(5)
        return BaseHelper.driver
    
    #初始化夜神模拟器
    def get_yeshen_driver(self):
        #DesiredCapabilities cap = new DesiredCapabilities(); 
        #cap.setCapability(CapabilityType.BROWSER_NAME, ""); 
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #指定测试平台
        desired_caps['deviceName'] = "127.0.0.1:62001"
        #指定测试机的ID,通过adb命令`adb devices`获取
        desired_caps['platformVersion'] = "4.4.2" 
        #使用unicode编码，以及在关闭后重置设备的默认输入法
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        #将上面获取到的包名和Activity名设置为值 
        desired_caps['appPackage'] = 'com.dbljoy.lottery' 
        desired_caps['appActivity'] = '.ui.activities.TransitionActivity'
        #A new session could not be created的解决方法
        #cap.setCapability("appWaitActivity",twoActivity); 
        #cap.setCapability("appWaitActivity",".MainActivity"); 
        #每次启动时覆盖session，否则第二次后运行会报错不能新建session 
        #cap.setCapability("sessionOverride", true); 
        BaseHelper.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        #adDriver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
        print("设备初始化成功")
        time.sleep(5)
        return BaseHelper.driver