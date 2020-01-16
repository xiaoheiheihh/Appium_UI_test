# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 11:24
# @File    : test_1login.py
# @Software: PyCharm Community Edition

import unittest
import app_caps
from Pages.login_page import LoginPage
from Base import public
import time


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = app_caps.app_caps()
        cls.login = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_001(self):
        """获取手机权限"""
        if self.login.find_element(self.login.permission):
            for i in range(3):
                self.login.click_element(self.login.permission)
                time.sleep(3)
            el = self.login.find_element(self.login.editName)
            self.assertTrue(el)

    def test_login_002(self):
        """输入正确的手机号，错误的密码，登录失败"""
        self.login.login('13524564318', '1234567')
        message = '//*[contains(@text,"不匹配")]'
        toast_text = self.login.find_element_xpath(message).text
        self.assertEqual(toast_text,"账户名与密码不匹配，请重新输入")
        self.driver.get_screenshot_as_file(public.create_screenshot('login') + '/账户名与密码不匹配.jpg')

    def test_login_003(self):
        """输入未注册的手机号和密码，登录失败，弹框提示"""
        self.login.login('13456734890','123456')
        message = '//*[contains(@text,"不存在")]'
        toast_text = self.login.find_element_xpath(message).text
        self.assertEqual(toast_text,"账户名不存在，请重新输入")
        self.driver.get_screenshot_as_file(public.create_screenshot('login') + '/账户名不存在.jpg')

    def test_login_004(self):
        """密码可见"""
        content = '12345'
        self.login.img_see(content)
        password_text = self.login.get_password_text()
        self.assertEqual(password_text,content)
        self.driver.get_screenshot_as_file(public.create_screenshot('login')+'/密码可见.jpg')

    def test_login_005(self):
        """密码不可见"""
        content = '12345'
        self.login.img_see(content)
        password_text = self.login.get_password_text()
        self.assertIn('•',password_text)
        self.driver.get_screenshot_as_file(public.create_screenshot('login') + '/密码不可见.jpg')

    def test_login_006(self):
        """手机号一键删除"""
        self.login.delete_username('12345')
        self.driver.get_screenshot_as_file(public.create_screenshot('login')+'/手机号一键删除图标隐藏.jpg')
        text = self.login.find_element(self.login.imgClear)
        self.assertFalse(text)

    def test_login_007(self):
        """手机号一键删除图标显示"""
        self.login.input_username('123')
        self.assertTrue(self.login.find_element(self.login.imgClear))
        self.driver.get_screenshot_as_file(public.create_screenshot('login') + '/手机号一键删除图标显示.jpg')

    def test_login_008(self):
        """密码一键删除"""
        self.login.delete_password('12345')
        self.driver.get_screenshot_as_file(public.create_screenshot('login')+'/密码一键删除图标隐藏.jpg')

    def test_login_009(self):
        """密码一键删除图标显示"""
        self.login.input_password('123')
        self.driver.get_screenshot_as_file(public.create_screenshot('login') + '/密码一键删除图标显示.jpg')

    def test_login_010(self):
        """跳转到找回密码页"""
        self.login.find_password()
        self.assertEqual(self.login.button_reset(),'重置密码')
        self.login.ima_back()

    def test_login_011(self):
        """点击注册按钮"""
        self.login.register()
        self.assertEqual(self.login.get_register(),'注册')
        self.login.ima_back()

    def test_login_012(self):
        """不输入手机号码和密码，登录按钮置灰"""
        self.login.input_username('')
        self.login.input_password('')
        self.assertFalse(self.login.get_submit().is_enabled())

    def test_login_013(self):
        """输入手机号，密码不足6位时，登录按钮置灰"""
        self.login.input_username('123')
        self.login.input_password('12345')
        self.assertFalse(self.login.get_submit().is_enabled())

    def test_login_014(self):
        """输入正确的手机号和密码，登录成功"""
        self.login.login('13524564318','123456')
        home_page = self.login.find_element(self.login.home_page)
        self.assertEqual(home_page.text,'首页')


if __name__ == '__main__':
    unittest.main(verbosity=2)


