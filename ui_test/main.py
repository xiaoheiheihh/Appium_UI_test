# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:31
# @File    : main.py
# @Software: PyCharm Community Edition

import unittest
import HTMLTestRunner
import os
import time
from Base.public import delete_screenshot

now_time=time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def create_suite():
    file_path = os.path.join(os.path.abspath('.'),'TestCase')
    suite = unittest.defaultTestLoader.discover(start_dir=file_path)
    return suite

def run_test():
    report_dir='./test_report'
    os.makedirs(report_dir,exist_ok=True)
    delete_screenshot('screenshot')
    report_path = '{0}/{1}.html'.format(report_dir,now_time)
    fp=open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试',description='app UI自动化测试')
    runner.run(create_suite())

if __name__ == '__main__':
    run_test()
