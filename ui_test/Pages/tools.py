# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 15:30
# @File    : tools.py
# @Software: PyCharm Community Edition

import os
import yaml
import jinja2

base_path = os.path.dirname(__file__)
yamlPagePath = os.path.join(base_path,'pageelement')

def parseyaml():
    pageElement = {}
    for fpath,dirname,filename in os.walk(yamlPagePath):
        for name in filename:
            yaml_file_path = os.path.join(fpath,name)
            if '.yaml' in str(yaml_file_path):
                with open(yaml_file_path,'r',encoding='utf-8') as f:
                    page = yaml.safe_load(f)
                    pageElement.update(page)
    return pageElement

#提取yaml数据
def get_page_list(yamlpage):
    page_object = {}
    for page,names in yamlpage.items():
        loc_names = []
        #获取所有的localors定位方法
        locs = names['locators']
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object

#创建page.py
def create_pages_py(page_list):
    print(os.path.join(base_path,'templetpage'))
    template_loader = jinja2.FileSystemLoader(searchpath=base_path)  #设置文件系统加载器
    template_env = jinja2.Environment(loader=template_loader)   #创建一个文件系统加载器对象
    templateVars = {
        'page_list':page_list
    }
    template = template_env.get_template('templetpage')#获取一个模版文件
    with open(os.path.join(base_path,'page.py'),'w',encoding='utf-8') as f:
        f.write(template.render(templateVars))  #render用于接受变量，对模板进行渲染
        # f.write(template.render(page_list=page_list))     #渲染

#获取某一元素信息
def get_locator(class_name,method_name):
    pages = parseyaml()
    locators = pages[class_name]['locators']
    for locator in locators:
        # locator_list = []
        if locator['name'] == method_name:
            type_form = locator['type']
            value = locator['value']
            return type_form,value

if __name__ == '__main__':
    pass
    # a = get_locator('Login','手机号')
    # print(a)
    a=parseyaml()
    print(a)
    print(type(a))
    # b =get_page_list(a)
    # print(b)
    # c= create_pages_py(b)