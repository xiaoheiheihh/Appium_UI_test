# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 15:39
# @File    : 1test_2clock.py
# @Software: PyCharm Community Edition

import unittest
from Pages.time_management import TimeManagement
import app_caps
import time
from Base.public import create_screenshot

class Clock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = app_caps.app_caps()
        cls.clock = TimeManagement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_clock_001(self):
        """进入到闹钟页面"""
        time.sleep(4)
        self.clock.enter_into(self.clock.iv_time)

    def test_clock_002(self):
        """设置过去的时间"""
        self.clock.enter_add()
        self.clock.enter_time()
        self.clock.swipe_down()
        self.clock.btn_submit()
        self.clock.save()
        toast_text = self.clock.find_element(self.clock.future_time).text
        self.assertEqual(toast_text,"只能设置未来时间的闹钟")
        self.clock.cancel()

    def test_clock_003(self):
        """设置当天单次闹钟"""
        self.clock.delete_all()
        set_time = self.clock.set_intraday_clock()
        time.sleep(1)
        date_time = self.clock.get_current_date()
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message,set_time)
        self.assertEqual('单次/'+date_time,repeat_type_message)
        # self.assertEqual(repeat_mode,'true')

    def test_clock_004(self):
        """设置指定日期的单次闹钟"""
        self.clock.delete_all()
        time_set, date_time = self.clock.set_month_year_clock(0)
        toast_text = self.clock.find_element(self.clock.set_success).text
        self.assertEqual(toast_text,"设置成功")
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message,time_set)
        self.assertIn('单次/'+date_time,repeat_type_message)
        # self.assertEqual(repeat_mode,'true')

    def test_clock_005(self):
        """设置每月的闹钟"""
        self.clock.delete_all()
        time_set, date_time = self.clock.set_month_year_clock(1)
        toast_text = self.clock.find_element(self.clock.set_success).text
        self.assertEqual(toast_text,"设置成功")
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message,time_set)
        self.assertIn('每月/'+date_time,repeat_type_message)
        # self.assertEqual(repeat_mode,'true')

    def test_clock_006(self):
        """设置每年的闹钟"""
        self.clock.delete_all()
        time_set, date_time = self.clock.set_month_year_clock(2)
        toast_text = self.clock.find_element(self.clock.set_success).text
        self.assertEqual(toast_text,"设置成功")
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message,time_set)
        self.assertIn('每年/'+date_time,repeat_type_message)
        # self.assertEqual(repeat_mode,'true')

    def test_clock_007(self):
        """设置每周一的闹钟"""
        self.clock.delete_all()
        set_time = self.clock.set_weekly_clock(0)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(repeat_type_message, '每周一')
        # self.assertEqual(repeat_mode, 'true')

    def test_clock_008(self):
        """设置每周一、三、五的闹钟"""
        self.clock.delete_all()
        set_time = self.clock.set_weekly_clock(0,2,4)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(repeat_type_message, '每周一/三/五')
        # self.assertEqual(repeat_mode, 'true')

    def test_clock_009(self):
        """设置每周工作日的闹钟"""
        self.clock.delete_all()
        set_time = self.clock.set_weekly_clock(0,1,2,3,4)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(repeat_type_message, '工作日')
        # self.assertEqual(repeat_mode, 'true')

    def test_clock_010(self):
        """设置周末的闹钟"""
        self.clock.delete_all()
        set_time = self.clock.set_weekly_clock(5,6)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(repeat_type_message, '周末')
        # self.assertEqual(repeat_mode, 'true')

    def test_clock_011(self):
        """设置每天的闹钟"""
        self.clock.delete_all()
        set_time = self.clock.set_weekly_clock(0,1,2,3,4,5,6)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.clock.get_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(repeat_type_message, '每天')
        # self.assertEqual(repeat_mode, 'true')

    def test_clock_012(self):
        """从编辑页面删除闹钟"""
        self.clock.delete_from_modify()
        toast_text = self.clock.find_element(self.clock.set_success).text
        self.assertEqual(toast_text,'设置成功')

    def test_clock_013(self):
        """关闭当天的单次闹钟"""
        self.clock.delete_all()
        self.clock.set_intraday_clock()
        message = self.clock.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('clock') + '/关闭当天的单次闹钟.jpg')
        # self.assertEqual(message,'false')

    def test_clock_014(self):
        """关闭指定日期的闹钟"""
        self.clock.delete_all()
        self.clock.set_month_year_clock(0)
        *other, message = self.clock.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('clock') + '/关闭指定日期闹钟.jpg')
        # self.assertEqual(message,'false')

    def test_clock_015(self):
        """关闭每月的闹钟"""
        self.clock.delete_all()
        self.clock.set_month_year_clock(1)
        *other, message = self.clock.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('clock') + '/关闭每月闹钟.jpg')
        time.sleep(10)
        # self.assertEqual(message,'false')

    def test_clock_016(self):
        """关闭每年的闹钟"""
        self.clock.delete_all()
        self.clock.set_month_year_clock(2)
        *other, message = self.clock.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('clock') + '/关闭每年闹钟.jpg')
        # self.assertEqual(message,'false')

    def test_clock_017(self):
        """删除所有闹钟"""
        self.clock.delete_all()
        toast_text = self.clock.find_element(self.clock.tvEmptyTip).text
        self.assertEqual(toast_text,'数据空空如也')

    def test_clock_018(self):
        """设置时间，重复类型，提醒内容完全一致的闹钟"""
        self.clock.delete_all()
        self.clock.set_weekly_clock(0)
        time.sleep(2)
        self.clock.set_weekly_clock(0)
        toast_text = self.clock.find_element(self.clock.already_exist).text
        self.assertEqual(toast_text,'闹钟已经存在')

    def test_clock_019(self):
        """设置超过200个闹钟，检查提示语"""
        for i in range(50):
            self.clock.set_time_submit()
            self.clock.set_weekly_clock()
            self.clock.set_month_year_clock(1)
            self.clock.set_intraday_clock()
        self.clock.enter_add()
        message_text = self.clock.find_element(self.clock.over_limit).text
        self.assertEqual(message_text,'数量超限喽')


if __name__ == '__main__':
    unittest.main(verbosity=2)
