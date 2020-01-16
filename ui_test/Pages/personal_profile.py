# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 17:55
# @File    : personal_profile.py
# @Software: PyCharm Community Edition

from Base.base_page import BasePage
import time
import datetime
from Pages.tools import get_locator

class PersonalCenterPage(BasePage):
    imgUser = get_locator('Personal_Center','个人中心')
    ivHeadImg = get_locator('Personal_Center', '头像')
    tvUserNick = get_locator('Personal_Center', '昵称')
    tvUserGender = get_locator('Personal_Center', '性别')
    tvUserBirthday = get_locator('Personal_Center', '生日')
    tvUserPhone = get_locator('Personal_Center', '手机号')
    rlModifyUserPassword = get_locator('Personal_Center', '修改密码')
    iv_photo = get_locator('Personal_Center', '头像_相机')
    shutter_button = get_locator('Personal_Center', '拍照键')
    btn_review_cancel = get_locator('Personal_Center', '头像_取消使用')
    done_button = get_locator('Personal_Center', '头像_使用')
    btnFinish = get_locator('Personal_Center', '完成键')
    btnRotate = get_locator('Personal_Center', '旋转键')
    etNickName = get_locator('Personal_Center', '昵称输入框')
    tvRight = get_locator('Personal_Center', '保存')
    btnLoginOut = get_locator('Personal_Center', '退出登录')
    buttonReset = get_locator('Personal_Center', '重置密码')
    upload_successful = get_locator('Personal_Center', '上传成功')
    titleName = get_locator('Personal_Center','个人信息')
    editName = get_locator('Login', '手机号')


    def __init__(self,driver):
        super(PersonalCenterPage,self).__init__(driver)

    def click_cancel(self):
        self.btn_cancel()

    #设置头像时，点击完成键
    def click_finish(self):
        self.click_element(PersonalCenterPage.btnFinish)

    def click_shutter(self):
        self.click_element(PersonalCenterPage.shutter_button)

    #拍照设置头像时，拍照后，点击左上角的×
    def click_review_cancel(self):
        self.click_element(PersonalCenterPage.btn_review_cancel)

    # 拍照设置头像时，拍照后，点击右上角的√
    def click_done(self):
        self.click_element(PersonalCenterPage.done_button)

    #通过手机的相机设置头像
    def set_image_camera(self,num):
        self.click_element(PersonalCenterPage.ivHeadImg)
        time.sleep(1)
        iv_photos = self.find_elements(PersonalCenterPage.iv_photo)
        iv_photos[num].click()
        # self.driver.find_elements_by_id('com.unisound.unione.phone:id/iv_photo')[0].click()
        time.sleep(2)
        self.click_shutter()
        time.sleep(2)
        self.click_done()
        time.sleep(2)
        self.click_finish()

    #手机相册中的图片设置头像
    def set_image_photo(self,num):
        self.click_element(PersonalCenterPage.ivHeadImg)
        iv_photos = self.find_elements(PersonalCenterPage.iv_photo)
        iv_photos[num].click()
        time.sleep(2)
        self.click_finish()

    #设置昵称
    def set_nick(self,element):
        self.click_element(PersonalCenterPage.tvUserNick)
        self.send_key(PersonalCenterPage.etNickName,element)
        self.click_element(PersonalCenterPage.tvRight)

    #获取昵称
    def get_nick(self):
        return self.find_element(PersonalCenterPage.tvUserNick).text

    #取消设置昵称
    def cancel_set_nick(self,element):
        self.click_element(PersonalCenterPage.tvUserNick)
        self.send_key(PersonalCenterPage.etNickName,element)
        self.im_back()

    #返回操作
    def back(self,element):
        self.click_element(element)

    #设置性别
    def set_gender(self):
        self.click_element(PersonalCenterPage.tvUserGender)

    #设置生日-年
    def set_year(self):
        self.swipe(x=0.1,y=0.9,y1=0.85,x1=0.1)

    #设置生日-月
    def set_month(self):
        self.swipe(x=0.4, y=0.9, y1=0.85, x1=0.4)

    #设置生日-日
    def set_day(self):
        self.swipe(x=0.7, y=0.9, y1=0.85, x1=0.7)

    #设置生日
    def set_birthday(self):
        self.click_element(PersonalCenterPage.tvUserBirthday)
        time.sleep(1)
        self.set_year()
        time.sleep(1)
        self.set_month()
        time.sleep(1)
        self.set_day()
        self.btn_submit()
        time.sleep(5)

    #获取当前的生日
    def get_cur_birthday(self):
        birthday_cur = str(self.find_element(PersonalCenterPage.tvUserBirthday).text)
        year, month, day= birthday_cur.split('-')
        return int(year),int(month),int(day)

    #获取当天的日期
    def get_cur_day(self):
        year_now =datetime.datetime.now().year
        month_now = datetime.datetime.now().month
        day_now = datetime.datetime.now().day
        return year_now,month_now,day_now

    #生日设置为当天的日期
    def set_cur_day(self):
        year_old,month_old,day_old = self.get_cur_birthday()
        year_now,month_now,day_now = self.get_cur_day()
        year_times = year_now - year_old
        month_times = month_now - month_old
        day_times = day_now - day_old
        for year in range(year_times):
            self.set_year()
        for month in range(month_times):
            self.set_month()
        for day in range(day_times):
            self.set_day()
        self.btn_submit()

    # 将手机号中间4位转换为*
    def phone_num(self,phonenum):
        new_num = []
        for i in range(len(phonenum)):
            new_num.append(phonenum[i])
        for j in range(3, 7):
            new_num[j] = '*'
        return ''.join(new_num)

    #获取手机号码
    def get_telephone(self):
        return self.find_element(PersonalCenterPage.tvUserPhone).text

    #修改密码
    def modify_password(self):
        self.click_element(PersonalCenterPage.rlModifyUserPassword)
        reset_button =self.find_element(PersonalCenterPage.buttonReset)
        return reset_button

    def modify_password_back(self):
        self.ima_back()

    #确定退出
    def logout_submit(self):
        self.click_element(PersonalCenterPage.btnLoginOut)
        time.sleep(1)
        self.popup_submit()

    #取消退出
    def logout_cancel(self):
        self.click_element(PersonalCenterPage.btnLoginOut)
        time.sleep(1)
        self.popup_cancel()

    # def enter_into_manual(self, content):
    #     self.click_element(PersonalCenterPage.stvUserGuide)
    #     element = get_locator('User_Manual', content)
    #     self.find_element(element).click()
    #     content_list = ['配置网络', '唤醒音箱', '免唤醒词', '产品外观', '蓝牙连接', '音量调节']
    #     for i in range(len(content_list)):
    #         if i==0 and content==content_list[i]:
    #             next_content = content_list[i + 1]
    #             return next_content
    #         elif i==(len(content_list)-1) and content==content_list[i]:
    #             pre_content = content_list[i-1]
    #             return pre_content
    #         else:
    #             next_content = content_list[i + 1]
    #             pre_content = content_list[i - 1]
    #             return next_content,pre_content


# if __name__ == '__main__':
#     num = phone_num('13524564318')
#     print(num)





