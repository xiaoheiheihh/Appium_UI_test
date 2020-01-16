# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 11:27
# @File    : app_caps.py
# @Software: PyCharm Community Edition

from appium import webdriver

def app_caps():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'WTKDU16926003981'
    # desired_caps['autoGrantPermissions'] = True
    desired_caps['appPackage'] = 'com.unisound.unione.phone'
    desired_caps['appActivity'] = '.ui.FlashActivity'
    desired_caps['noReset'] = 'True'
    desired_caps['resetKeyboard'] = 'true'
    desired_caps['unicodeKeyboard'] = 'true'
    desired_caps['automationName'] = 'uiautomator2'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


