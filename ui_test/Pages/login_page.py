# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:52
# @File    : login_page.py
# @Software: PyCharm Community Edition

from Base.base_page import BasePage
from app_caps import app_caps
from Pages.tools import get_locator


class LoginPage(BasePage):
    editName= get_locator('Login', '手机号')
    editPassword= get_locator('Login', '密码')
    btnLogin= get_locator('Login', '登录')
    imgSee= get_locator('Login', '密码可见图标')
    imgClear= get_locator('Login', '用户名一键删除图标')
    ivClear= get_locator('Login', '密码一键删除图标')
    textFindPassword= get_locator('Login', '忘记密码')
    tvRegister= get_locator('Login', '还没有账号_点击注册')
    buttonReset= get_locator('Login', '重置密码按钮')
    buttonRegist= get_locator('Login', '注册')

    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)

    #输入手机号
    def input_username(self,username):
        self.send_key(LoginPage.editName,username)

    #输入密码
    def input_password(self,password):
        self.send_key(LoginPage.editPassword,password)

    def get_submit(self):
        return self.find_element(LoginPage.btnLogin)

    #登录
    def login(self,username='',password=''):
        self.input_username(username)
        self.input_password(password)
        self.click_element(LoginPage.btnLogin)

    #密码可见图标点击
    def img_see(self,content):
        self.send_key(LoginPage.editPassword,content)
        self.click_element(LoginPage.imgSee)

    #获取密码框的文本
    def get_password_text(self):
        return self.find_element(LoginPage.editPassword).text

    #获取用户名的文本
    def get_username_text(self):
        return self.find_element(LoginPage.editName).text

    #用户名一键删除
    def delete_username(self,content):
        self.send_key(LoginPage.editName,content)
        self.click_element(LoginPage.imgClear)

    #密码一键删除
    def delete_password(self,content):
        self.send_key(LoginPage.editPassword,content)
        self.click_element(LoginPage.ivClear)

    #一键删除图标显示
    def delete_img(self,element):
        self.send_key(element,'1')

    #点击找回密码
    def find_password(self):
        self.click_element(LoginPage.textFindPassword)

    #获取重置按钮的文本
    def button_reset(self):
        return self.find_element(LoginPage.buttonReset).text

    #注册
    def register(self):
        self.click_element(LoginPage.tvRegister)

    #获取注册文本
    def get_register(self):
        return self.find_element(LoginPage.buttonRegist).text


if __name__ == '__main__':
    login_ob = LoginPage(app_caps())
    login_ob.login('1234567890','0987654321')















