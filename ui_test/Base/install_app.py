# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 13:53
# @File    : install_app.py
# @Software: PyCharm Community Edition

import time
import os
from threading import Thread
from app_caps import app_caps

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

def installApp():
    os.popen("adb install"+PATH('UniOnePhone-debug-v1.4.8-20190815-2ebe2393.apk'))

def inputEvent():
    time.sleep(5)
    os.popen("adb shell input tap 785 1280")

def install():
    t1=Thread(target=installApp)
    t2=Thread(target=inputEvent())
    t1.start()
    t2.start()

if __name__ == '__main__':
    driver = app_caps()
    install()
