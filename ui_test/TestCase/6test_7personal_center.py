# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 19:38
# @File    : test_7personal_center.py
# @Software: PyCharm Community Edition

from Pages.personal_profile import PersonalCenterPage
import unittest
import app_caps
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
from Base.public import is_leapyear

class PersonalCenter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = app_caps.app_caps()
        cls.personal = PersonalCenterPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_personal_001(self):
        """切换到个人中心"""
        self.personal.click_element(self.personal.navigation_user)
        self.personal.click_element(self.personal.imgUser)

    def test_personal_002(self):
        """通过本地照片拍照设置头像"""
        self.personal.set_image_photo(1)
        toast_text = self.personal.find_element(self.personal.upload_successful).text
        self.assertEqual(toast_text,'上传成功！')
        time.sleep(2)

    def test_personal_003(self):
        """通过相机拍照设置头像"""
        self.personal.set_image_camera(0)
        toast_text = self.personal.find_element(self.personal.upload_successful).text
        self.assertEqual(toast_text,'上传成功！')
        time.sleep(2)

    def test_personal_004(self):
        """设置英文昵称"""
        nick = 'candy'
        self.personal.set_nick(nick)
        self.assertEqual(self.personal.get_nick(),nick)

    def test_personal_005(self):
        """设置中文昵称"""
        nick = '你好魔方'
        self.personal.set_nick(nick)
        self.assertEqual(self.personal.get_nick(),nick)

    def test_personal_006(self):
        """设置中英文混合昵称"""
        nick = 'hello你好'
        self.personal.set_nick(nick)
        self.assertEqual(self.personal.get_nick(),nick)

    def test_personal_007(self):
        """设置特殊字符昵称"""
        nick = '@#￥%&*（'
        self.personal.set_nick(nick)
        self.assertEqual(self.personal.get_nick(),nick)

    def test_personal_008(self):
        """取消设置昵称"""
        nick = self.personal.get_nick()
        nick_change = '你好'
        self.personal.cancel_set_nick(nick_change)
        self.assertEqual(self.personal.get_nick(),nick)

    def test_personal_009(self):
        """设置生日"""
        self.personal.set_birthday()
        year_now,month_now,day_now = self.personal.get_cur_birthday()
        self.assertTrue(int(year_now)>= 1900 or int(year_now)<=datetime.datetime.now().year)
        if year_now ==datetime.datetime.now().year:
            self.assertTrue(int(month_now)>= 1 or int(month_now) <= datetime.datetime.now().month)
        else:
            self.assertTrue(int(month_now) >= 1 or int(month_now) <= 12)

        if year_now ==datetime.datetime.year and month_now == datetime.datetime.now().month:
            self.assertTrue(int(day_now) >= 1 or int(day_now) <= datetime.datetime.now().day)
        else:
            self.assertTrue(int(day_now) >= 1 or int(day_now) <= 31)


    def test_personal_010(self):
        """检查手机号码显示"""
        phone_text = self.personal.get_telephone()
        self.assertEqual(phone_text,self.personal.phone_num('13524564318'))

    def test_personal_011(self):
        """进入到重置密码界面，检查重置秘密按钮是否可点击"""
        reset = self.personal.modify_password()
        self.assertFalse(reset.is_enabled())
        self.personal.modify_password_back()

    def test_personal_012(self):
        """取消退出登录"""
        self.personal.logout_cancel()
        self.assertTrue(self.personal.find_element(self.personal.titleName))

    def test_personal_013(self):
        """确定退出登录"""
        self.personal.logout_submit()
        self.assertTrue(self.personal.find_element(self.personal.editName))


if __name__ == '__main__':
    unittest.main(verbosity=2)






