# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 15:15
# @File    : test_3note.py
# @Software: PyCharm Community Edition

import unittest
from Pages.time_management import TimeManagement
import app_caps
import time
from Base.public import create_screenshot

class Note(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = app_caps.app_caps()
        cls.note = TimeManagement(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_note_001(self):
        """进入到日程页面"""
        time.sleep(4)
        self.note.enter_into(self.note.iv_note)

    def test_note_002(self):
        """主题为空时，点击保存"""
        self.note.enter_add()
        self.note.set_time_submit()
        self.note.save()
        toast_text = self.note.find_element(self.note.forgot_title).text
        self.assertEqual(toast_text,"不要忘记填写主题哟")
        self.note.cancel()

    def test_note_003(self):
        """设置过去的时间"""
        self.note.enter_add()
        self.note.set_title('吃饭')
        self.note.enter_time()
        self.note.swipe_down()
        self.note.btn_submit()
        self.note.save()
        toast_text = self.note.find_element(self.note.future_time).text
        self.assertEqual(toast_text,"只能设置未来时间的日程")
        self.note.cancel()

    def test_note_004(self):
        """设置当天单次提醒"""
        self.note.delete_all()
        content = '吃晚饭'
        set_time = self.note.set_intraday_note(content)
        time.sleep(1)
        date_time = self.note.get_current_date()
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message,set_time)
        self.assertEqual(note_message,content)
        self.assertEqual('单次/'+date_time,repeat_type_message,)
        # self.assertEqual(repeat_mode,'true')

    def test_note_005(self):
        """设置指定日期的单次提醒"""
        self.note.delete_all()
        content = '喝水'
        time_set, date_time = self.note.set_month_year_note(content,0)
        toast_text = self.note.find_element(self.note.set_success).text
        self.assertEqual(toast_text,"设置成功")
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message,time_set)
        self.assertEqual(note_message,content)
        self.assertIn('单次/'+date_time,repeat_type_message)
        # self.assertEqual(repeat_mode,'true')

    def test_note_006(self):
        """设置每月的提醒"""
        self.note.delete_all()
        content = '吃饭'
        time_set, date_time = self.note.set_month_year_note(content,1)
        toast_text = self.note.find_element(self.note.set_success).text
        self.assertEqual(toast_text,"设置成功")
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message,time_set)
        self.assertEqual(note_message,content)
        self.assertIn('每月/'+date_time,repeat_type_message)
        # self.assertEqual(repeat_mode,'true')

    def test_note_007(self):
        """设置每年的提醒"""
        self.note.delete_all()
        content = '锻炼'
        time_set, date_time = self.note.set_month_year_note(content, 2)
        toast_text = self.note.find_element(self.note.set_success).text
        self.assertEqual(toast_text,"设置成功")
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message,time_set)
        self.assertEqual(note_message,content)
        self.assertIn('每年/'+date_time,repeat_type_message)
        # self.assertEqual(repeat_mode,'true')

    def test_note_008(self):
        """设置每周一的提醒"""
        self.note.delete_all()
        content = '喝水'
        set_time = self.note.set_weekly_note(content,0)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(note_message, content)
        self.assertEqual(repeat_type_message, '每周一')
        # self.assertEqual(repeat_mode, 'true')

    def test_note_009(self):
        """设置每周一、三、五的提醒"""
        self.note.delete_all()
        content = '喝水'
        set_time = self.note.set_weekly_note(content, 0,2,4)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(note_message, content)
        self.assertEqual(repeat_type_message, '每周一/三/五')
        # self.assertEqual(repeat_mode, 'true')

    def test_note_010(self):
        """设置每周工作日的提醒"""
        self.note.delete_all()
        content = '喝水'
        set_time = self.note.set_weekly_note(content, 0,1,2,3,4)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(note_message, content)
        self.assertEqual(repeat_type_message, '工作日')
        # self.assertEqual(repeat_mode, 'true')

    def test_note_011(self):
        """设置周末的提醒"""
        self.note.delete_all()
        content = '喝水'
        set_time = self.note.set_weekly_note(content, 5,6)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(note_message, content)
        self.assertEqual(repeat_type_message, '周末')
        # self.assertEqual(repeat_mode, 'true')

    def test_note_012(self):
        """设置每天的提醒"""
        self.note.delete_all()
        content = '喝水'
        set_time = self.note.set_weekly_note(content, 0,1,2,3,4,5,6)
        time.sleep(1)
        time_message, repeat_type_message, repeat_mode = self.note.get_message()
        note_message = self.note.get_note_message()
        self.assertEqual(time_message, set_time)
        self.assertEqual(note_message, content)
        self.assertEqual(repeat_type_message, '每天')
        # self.assertEqual(repeat_mode, 'true')

    def test_note_013(self):
        """从编辑页面删除提醒"""
        self.note.delete_from_modify()
        toast_text = self.note.find_element(self.note.set_success).text
        self.assertEqual(toast_text,'设置成功')

    def test_note_014(self):
        """关闭当天的单次提醒"""
        self.note.delete_all()
        content = '吃晚饭'
        self.note.set_intraday_note(content)
        message = self.note.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('note') + '/关闭当天的单次提醒.jpg')
        # self.assertEqual(message,'false')

    def test_note_015(self):
        """关闭指定日期的提前"""
        self.note.delete_all()
        self.note.set_month_year_note('吃饭',0)
        *other, message = self.note.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('note') + '/关闭指定日期提醒.jpg')
        # self.assertEqual(message,'false')

    def test_note_016(self):
        """关闭每月的提醒"""
        self.note.delete_all()
        self.note.set_month_year_note('吃饭',1)
        *other, message = self.note.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('note') + '/关闭每月提醒.jpg')
        # self.assertEqual(message,'false')

    def test_note_017(self):
        """关闭每年的提醒"""
        self.note.delete_all()
        self.note.set_month_year_note('吃饭',2)
        *other, message = self.note.turn_on_off()
        self.driver.get_screenshot_as_file(create_screenshot('note') + '/关闭每年提醒.jpg')
        # self.assertEqual(message,'false')

    def test_note_018(self):
        """删除所有提醒"""
        self.note.delete_all()
        toast_text = self.note.find_element(self.note.tvEmptyTip).text
        self.assertEqual(toast_text,'数据空空如也')

    def test_note_019(self):
        """设置时间，重复类型，提醒内容完全一致的提醒"""
        self.note.delete_all()
        content = '吃饭'
        self.note.set_weekly_note(content,0)
        time.sleep(2)
        self.note.set_weekly_note(content,0)
        toast_text = self.note.find_element(self.note.already_exist).text
        self.assertEqual(toast_text,'日程已经存在')

    # def test_note_020(self):
    #     """设置超过200个提醒，检查提示语"""
    #     self.note.enter_into(self.note.iv_note)
    #     self.note.delete_all()
    #     for i in range(40):
    #         content_list = ['吃饭','喝水','逛街','锻炼','逛超市']
    #         for j in range(len(content_list)):
    #             self.note.set_weekly_note(content_list[j],1)
    #             time.sleep(2)
    #     self.note.enter_add()
    #     message_text = self.note.find_element(self.note.over_limit).text
    #     self.assertEqual(message_text,'数量超限喽')

if __name__ == '__main__':
    unittest.main(verbosity=2)
