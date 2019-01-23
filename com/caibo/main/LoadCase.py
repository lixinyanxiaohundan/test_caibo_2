import os
import unittest

cash_path = os.path.join(os.getcwd(),'../case')

print('文件地址：', os.getcwd())
print("cash_path:", cash_path)

discover = unittest.defaultTestLoader.discover(cash_path,
                                               pattern="Test_*.py",
                                               top_level_dir=None)
# top_level_dir : 这个是顶层目录的名称，一般默认等于None就行了

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)