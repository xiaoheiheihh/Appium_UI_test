# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 18:58
# @File    : time_management.py
# @Software: PyCharm Community Edition

from Base.base_page import BasePage
from Pages.tools import get_locator
import datetime
import time
from app_caps import app_caps

class TimeManagement(BasePage):
    iv_note = get_locator('Time_Management', '日程')
    iv_time = get_locator('Time_Management', '闹钟')
    iv_iot = get_locator('Time_Management', '倒计时')
    itemLabContent = get_locator('Time_Management', '主题输入框')
    rightImage = get_locator('Time_Management', '新建按钮')
    titleRight = get_locator('Time_Management', '保存')
    titleLeft = get_locator('Time_Management', '取消')
    itemTimeContent = get_locator('Time_Management', '时间')
    itemRepeatContent = get_locator('Time_Management', '重复')
    selectDate = get_locator('Time_Management', '选择日期')
    btnDelete = get_locator('Time_Management', '删除')
    tvTime = get_locator('Time_Management', '时间管理页_时间')
    tvLab = get_locator('Time_Management', '时间管理页_主题')
    tvRepeatType = get_locator('Time_Management', '时间管理页_重复方式')
    ivChange = get_locator('Time_Management', '时间管理页_开关状态')
    tvRepeatExtraTypeContent = get_locator('Time_Management', '一次，每月循环，每年循环')
    tv_repeat_type = get_locator('Time_Management', '每周')
    tvEmptyTip = get_locator('Time_Management','数据空空如也')
    future_time = get_locator('Time_Management', '只能设置未来时间的闹钟')
    set_success = get_locator('Time_Management', '设置成功')
    already_exist = get_locator('Time_Management', '闹钟已存在')
    over_limit = get_locator('Time_Management', '数量超限喽')
    forgot_title = get_locator('Time_Management', '不要忘记填写主题哟')

    def __init__(self,driver):
        super(TimeManagement,self).__init__(driver)

    #点击新增按钮
    def enter_add(self):
        self.click_element(TimeManagement.rightImage)

    #输入主题内容
    def set_title(self,content):
        self.send_key(TimeManagement.itemLabContent,content)

    # 滑动设置时间--小时
    def set_time_hour(self,x1=0.4, y1=0.9, x2=0.4, y2=0.85):
        # self.swipe(x=0.4, y=0.9, x1=0.4, y1=0.85)
        self.swipe(x1, y1, x2, y2)

    # 滑动设置时间--分钟
    def set_time_min(self,x1=0.8, y1=0.9, x2=0.8, y2=0.85):
        # self.swipe(x=0.8, y=0.9, x1=0.8, y1=0.85)
        self.swipe(x1, y1, x2, y2)

    # 滑动设置日期--年
    def set_date_year(self):
        self.swipe(x=0.2, y=0.9, x1=0.2, y1=0.85)

    # 滑动设置日期--月
    def set_date_month(self):
        self.swipe(x=0.45, y=0.9, x1=0.45, y1=0.85)

    # 滑动设置日期--日
    def set_date_day(self):
        self.swipe(x=0.9, y=0.9, x1=0.9, y1=0.85)

    #设置时间--确定
    def set_time_submit(self):
        # self.enter_into(self.iv_time)
        # self.enter_add()
        time_now = self.get_settime()
        time_min = time_now.split(':')[1]
        self.enter_time()
        time.sleep(1)
        if time_min ==59:
            self.set_time_hour(y2=0.8)
            self.set_time_min(y1=0.85,y2=0.9)
        else:
            self.set_time_hour()
            self.set_time_min()
        # print(time_now)
        # self.set_time_hour()
        # self.set_time_min()
        self.btn_submit()

    #设置时间--取消
    def set_time_cancel(self):
        self.enter_time()
        time.sleep(1)
        self.set_time_hour()
        self.set_time_min()
        self.cancel()

    #进入到时间设置页
    def enter_time(self):
        self.click_element(TimeManagement.itemTimeContent)

    #进入重复页面
    def enter_repeat(self):
        self.click_element(TimeManagement.itemRepeatContent)

    #进入到日期选择页面
    def enter_select_date(self):
        self.click_element(TimeManagement.selectDate)

    #一次/每月/每年 页面的操作
    def set_repeat(self,num):
        repeat_mode = self.get_repeat_mode()
        time.sleep(1)
        repeat_mode[num].click()
        self.enter_select_date()
        time.sleep(1)
        if num ==0:
            self.set_date_year()
            self.set_date_month()
            self.set_date_day()
        elif num ==1:
            self.set_date_day()
        elif num ==2:
            self.set_date_month()
            self.set_date_day()
        else:
            pass
        time.sleep(2)
        self.btn_submit()

    #每周一到周日 页面的操作
    def set_weekly(self,*num):
        repeat_mode = self.get_repeat_mode_week()
        for i in range(len(num)):
            repeat_mode[num[i]].click()

    #设置一次/每月/每年的提醒
    def set_month_year_note(self,content,num):
        self.enter_add()
        self.set_title(content)
        self.set_time_submit()
        time_set = self.get_settime()
        self.enter_repeat()
        self.set_repeat(num)
        date_time = self.get_setdate(num)
        self.im_back()
        self.save()
        return time_set,date_time

    #设置一次/每月/每年的闹钟
    def set_month_year_clock(self,num):
        self.enter_add()
        self.set_time_submit()
        time_set = self.get_settime()
        self.enter_repeat()
        self.set_repeat(num)
        date_time = self.get_setdate(num)
        self.im_back()
        self.save()
        return time_set,date_time

    #设置每周的提醒
    def set_weekly_note(self,content,*num):
        self.enter_add()
        self.set_title(content)
        self.set_time_submit()
        set_time = self.get_settime()
        self.enter_repeat()
        self.set_weekly(*num)
        self.im_back()
        self.save()
        return set_time

    #设置每周的闹钟
    def set_weekly_clock(self,*num):
        self.enter_add()
        self.set_time_submit()
        set_time = self.get_settime()
        self.enter_repeat()
        self.set_weekly(*num)
        self.im_back()
        self.save()
        return set_time

    #设置当天的单次闹钟
    def set_intraday_clock(self):
        self.enter_add()
        self.set_time_submit()
        set_time = self.get_settime()
        self.save()
        return set_time

    #设置当天的单次提醒
    def set_intraday_note(self,content):
        self.enter_add()
        self.set_title(content)
        self.set_time_submit()
        set_time = self.get_settime()
        self.save()
        return set_time


    #获取循环模式(一次，选择日期，每年循环)，并返回一个列表
    def get_repeat_mode(self):
        return self.find_elements(TimeManagement.tvRepeatExtraTypeContent)

    #获取每周的循环方式，并返回一个列表
    def get_repeat_mode_week(self):
        return self.find_elements(TimeManagement.tv_repeat_type)

    #获取设置的时间
    def get_settime(self):
        return self.find_element(TimeManagement.itemTimeContent).text

    #获取设置成功的提醒内容
    def get_note_message(self):
        time.sleep(1)
        note_message = self.find_element(TimeManagement.tvLab).text
        return  note_message

    #获取时间，重复方式，状态的信息
    def get_message(self):
        time.sleep(1)
        time_message = self.find_element(TimeManagement.tvTime).text
        repeat_type_message = self.find_element(TimeManagement.tvRepeatType).text
        repeat_mode = self.find_element(TimeManagement.ivChange).get_attribute('checked')
        return time_message, repeat_type_message, repeat_mode

    #从编辑页面删除提醒，闹钟
    def delete_from_modify(self):
        time.sleep(2)
        elements = self.find_elements(TimeManagement.tvTime)
        time.sleep(1)
        elements[0].click()
        self.click_element(TimeManagement.btnDelete)

    #设置日期--取消
    def set_date_cancel(self,content,num):
        self.set_repeat(num)
        self.cancel()

    #设置日期--确定
    def set_date_submit(self,num):
        self.set_repeat(num)
        self.btn_submit()

    #获取设置的日期的内容，即一次，每月，每年循环时设置的日期，用于后续断言
    def get_setdate(self,num):
        date_time_cur = self.find_element(TimeManagement.selectDate).text
        if num == 0:
            date_list = str(date_time_cur).split('-')
            date_list.insert(1, '年')
            date_list.insert(3, '月')
            date_list.insert(5, '日')
            date_time = ''.join(date_list)
            return date_time
        elif num == 1:
            date_time = str(date_time_cur)
            return date_time
        else:
            date_time=str(date_time_cur)
            return date_time

    #获取现在的日期，并对日期进行格式化
    def get_current_date(self):
        time_list = []
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        time_list.append(str(year))
        time_list.append('年')
        if month < 10:
            time_list.append('0' + str(month))
        else:
            time_list.append(str(month))
        time_list.append('月')
        if day < 10:
            time_list.append('0' + str(day))
        else:
            time_list.append(str(day))
        time_list.append('日')
        date_time = ''.join(time_list)
        return date_time

    #删除所有的时间管理
    def delete_all(self):
        flag = True
        while flag:
            if not(self.find_element(TimeManagement.tvEmptyTip)):
                self.delete_from_modify()
            else:
                flag = False

    #点击打开关闭按钮
    def turn_on_off(self):
        element = self.find_elements(TimeManagement.ivChange)[0]
        element.click()
        time.sleep(3)
        *n,repeat_mode = self.get_message()
        return repeat_mode

    #保存提醒，即点击右上角的保存按钮
    def save(self):
        self.click_element(TimeManagement.titleRight)

    #取消设置时间管理，即点击左上角的返回按钮
    def cancel(self):
        self.click_element(TimeManagement.titleLeft)

    #提醒和闹钟的时间排序
    def time_sort(self):
        self.enter_into(TimeManagement.iv_time)
        time_element_list = self.find_elements(TimeManagement.tvTime)
        time_sort = []
        for i in range(len(time_element_list)):
            time_info = time_element_list[i].text
            time_list = ''.join(time_info.split(':'))
            time_sort.append(time_list)
        print('排序前的时间是:',time_sort)
        print('排序后的时间是:',sorted(time_sort,reverse=True))
        return time_sort

if __name__ == '__main__':
    time_m= TimeManagement(app_caps())
    # time_m.set_time_submit()
    time_m.time_sort()


















