# 测试报告


from work.xuqiu import login

import unittest

import sys

from package_unittest.HTMLTestRunner import HTMLTestRunner         #导入包

class TestLogin(unittest.TestCase):



    # 1. 测试登录的测试用例

    # case1 : 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 0          #期望值
        actual_value = login('admin','123456').get('code')        #实际值
        self.assertEqual(except_value,actual_value)

    # case2: 输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('bac','123456').get('code')
        self.assertEqual(except_value,actual_value)

    # case3 : 输入空的用户或密码登录
    def test_password_is_null(self):
        print("开始运行方法:", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)

if __name__ == '__main__':

        # 创建一个套件
    suita_a = unittest.TestSuite()
    suita_a.addTest(TestLogin('test_login_success'))
    suita_a.addTest(TestLogin('test_user_wrong'))
    suita_a.addTest(TestLogin('test_password_is_null'))
    print(suita_a)

    # 创建一个测试报告文件，是HTML格式
    test_report = './test_report.html'

    with open(test_report,'wb') as f:


        runner = HTMLTestRunner(f,title="测试报告",description="测试报告描述")
        runner.run(suita_a)
