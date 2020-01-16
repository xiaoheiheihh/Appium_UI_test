# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:31
# @File    : base_page.py
# @Software: PyCharm Community Edition

from selenium.webdriver.support.ui import WebDriverWait
from Pages.tools import get_locator
from selenium.common.exceptions import NoSuchElementException
from app_caps import app_caps

#封装appium基本方法

class BasePage(object):
    btnSubmit = get_locator('Base', '设置时间/日期_确定')
    btnCancel = get_locator('Base', '设置时间/日期_取消')
    submit = get_locator('Base', '弹框界面_确定')
    cancel = get_locator('Base', '弹框界面_取消')
    imBack = get_locator('Base', '左上角返回箭头')
    imaBack = get_locator('Base', '重置密码界面的返回箭头')
    home_page = get_locator('Base', '首页')
    navigation_home = get_locator('Base', 'home')
    navigation_user = get_locator('Base', '我的')
    permission = get_locator('Base', '手机权限')


    def __init__(self,driver):
        self.driver = driver

    def find_element(self,element):
        if element[0]=='id':
            try:
                return WebDriverWait(self.driver,5, 0.5).until(lambda x: x.find_element_by_id(element[1]))
            except Exception as e:
                return False
        elif element[0]=='xpath':
            try:
                return WebDriverWait(self.driver,5, 0.5).until(lambda x: x.find_element_by_xpath(element[1]))
            except Exception as e:
                return False

    def find_elements(self, element):
        if element[0] == 'id':
            try:
                return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_elements_by_id(element[1]))
            except Exception as e:
                return False
        else:
            pass

    # #通过xpath查找元素
    def find_element_xpath(self,message):
        return WebDriverWait(self.driver,7,0.5).until(lambda x:x.find_element_by_xpath(message))
    #
    # #重写查找元素集的方法
    # def find_elements(self,element):
    #     return WebDriverWait(self.driver, 7, 0.5).until(lambda x: x.find_elements_by_id(element))

    #重写点击方法
    def click_element(self,element):
        self.find_element(element).click()

    #重写发送内容方法
    def send_key(self,element,content):
        self.find_element(element).send_keys(content)

    def get_size(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width,height

    def swipe(self,x,y,x1,y1,t=1000):
        size = self.get_size()
        return self.driver.swipe(size[0]*x,size[1]*y,size[0]*x1,size[1]*y1,t)

    #日期设置界面_确定
    def btn_submit(self):
        self.click_element(BasePage.btnSubmit)

    # 日期设置界面_取消
    def btn_cancel(self):
        self.click_element(BasePage.btnCancel)

    #弹框界面，单击确定
    def popup_submit(self):
        self.click_element(BasePage.submit)
    #弹框界面，单击取消
    def popup_cancel(self):
        self.click_element(BasePage.cancel)

    #返回
    def im_back(self):
        self.click_element(BasePage.imBack)

    #重置密码界面，点击返回
    def ima_back(self):
        self.click_element(BasePage.imaBack)

    #进入到某页面，例如进入到闹钟，音乐等
    def enter_into(self,element):
        self.click_element(element)

    #返回到首页
    def back_to_home(self):
        for i in range(3):
            if not self.find_element(self.navigation_home):
                self.im_back()
            else:
                break

    #向上滑动
    def swipe_up(self,x1=0.2,y1=0.9,x2=0.2,y2=0.8,t=1000):
        size = self.get_size()
        x1 = size[0] * x1
        y1 = size[1] * y1
        x2 = size[0] * x2
        y2 = size[1] * y2
        self.driver.swipe(x1, y1, x2, y2, t)

    # 向下滑动
    def swipe_down(self,x1=0.3,y1=0.85,x2=0.3,y2=0.9,t=1000):
        size = self.get_size()
        x1 = size[0] * x1
        y1 = size[1] * y1
        x2 = size[0] * x2
        y2 = size[1] * y2
        self.driver.swipe(x1, y1, x2, y2, t)

    # 向左滑动
    def swipe_left(self,x1=0.9,y1=0.3,x2=0.7,y2=0.3,t=1000):
        size = self.get_size()
        x1 = size[0] * x1
        y1 = size[1] * y1
        x2 = size[0] * x2
        y2 = size[1] * y2
        self.driver.swipe(x1, y1, x2, y2, t)

    # 向右滑动
    def swipe_right(self,x1=0.25,y1=0.5,x2=0.75,y2=0.5,t=1000):
        size = self.get_size()
        x1 = size[0] * x1
        y1 = size[1] * y1
        x2 = size[0] * x2
        y2 = size[1] * y2
        self.driver.swipe(x1, y1, x2, y2, t)

if __name__ == '__main__':
    pass




