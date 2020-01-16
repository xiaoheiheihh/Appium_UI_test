# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 16:33
# @File    : public.py
# @Software: PyCharm Community Edition

import os
import shutil
import yaml
import logging.config

#判读是否为闰年
def is_leapyear(year):
    if year % 100 == 0:
        if year % 400 == 0:

            print('%d年是闰年' %year)

        else:

            print('%d年不是闰年' %year)
    else:
        if year%4==0:

            print('%d年是闰年' %year)
        else:

            print('%d年不是闰年' %year)

#创建截图路径
def create_screenshot(path):
    cur = os.path.dirname(os.path.dirname(__file__))
    screen_path = os.path.join(cur,'screenshot',path)
    os.makedirs(screen_path,exist_ok=True)
    return screen_path

#删除指定路径里面文件
def delete_screenshot(path):
    cur_path = os.path.dirname(os.path.dirname(__file__))
    dir_path = os.path.join(cur_path, path)
    filelist = os.listdir(dir_path)
    for f in filelist:
        file_path = os.path.join(dir_path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path, True)
        else:
            pass

def log_template(log_name='fileLogger'):
    path = os.path.dirname(__file__)
    yaml_path = os.path.join(path,'log.yaml')
    with open(yaml_path,'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        logger = logging.getLogger(log_name)
        return logger

if __name__ == '__main__':
    logger = log_template()
    logger.info('这是一个info文件')



