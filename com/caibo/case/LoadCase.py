# -*- coding: utf-8 -*-
import datetime,unittest,pytest
import sys
import os
os.chdir('C:/Users/Administrator/Desktop/py/TestPython1/test_caibo_2')
for file in os.listdir(os.getcwd()):
    print(file)
sys.path.append('../')
sys.path.append(r'/Users/Administrator/Desktop/py/TestPython1/test_caibo_2')
sys.path.append(r'/Users/Administrator/Desktop/py/TestPython1/test_caibo_2/com')
sys.path.append(r'/Users/Administrator/Desktop/py/TestPython1/test_caibo_2/com/caibo/case')
sys.path.append(r'/Users/Administrator/Desktop/py/TestPython1/test_caibo_2/com/caibo/api')
from test_caibo_2.com.caibo.api.Utils import Utils
from test_caibo_2.com.caibo.api.HTMLTestRunner import HTMLTestRunner


# rootpath=str("C:/Users/Administrator/Desktop/py/TestPython1/test_caibo_2")
# syspath=sys.path
# sys.path=[]
# sys.path.append(rootpath)  # 将工程根目录加入到python搜索路径中
# # 将工程目录下的一级目录添加到python搜索路径中
# sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0] != "."])
# sys.path.extend(syspath)

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
    
case_path=os.getcwd()
now_time = datetime.datetime.now().strftime('%Y_%m_%d')  # 当前日期,每天的报告放在每天的文件夹下
a = 'hello word'
b = a.replace('word','python')
temp_report_path=os.getcwd()
temp2_report_path=temp_report_path.replace('case','')
report_path = r"/Users/Administrator/Desktop/py/TestPython1/test_caibo_2/com/caibo/report/"+now_time # 存放报告路径
utils = Utils()
utils.mkdir(report_path)  #创建测试报告目录
utils.mkdir(r"/Users/Administrator/Desktop/py/TestPython1/test_caibo_2/com/caibo/screenShots/"+now_time)  # 创建截图目录


def creat_suite():
    uit = unittest.TestSuite()

    # 获取所有以test开头.py结尾的测试用例文件
    # discover = unittest.defaultTestLoader.discover(case_path, pattern="Test_*.py", top_level_dir=None)
    discover = unittest.defaultTestLoader.discover(r'/Users/Administrator/Desktop/py/TestPython1/test_caibo_2/com/caibo/case',
                                                   pattern="Test_*.py", top_level_dir=None)
    print(discover)
    # print (discover)
    # 遍历并执行每一个测试用例
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
            #print(test_case)
    return uit


# 执行测试
if __name__ == "__main__":
    suite = creat_suite()
    fb = open(r'/Users/Administrator/Desktop/py/TestPython1/test_caibo_2/com/caibo/report/'+now_time+'/result.html', 'wb')
    runner = HTMLTestRunner(stream=fb, title='caibo_test_report', description='paltfrom:Android')
    runner.run(suite)
    fb.close()
