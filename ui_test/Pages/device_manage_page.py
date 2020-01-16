# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 15:41
# @File    : device_manage_page.py
# @Software: PyCharm Community Edition
from Base.base_page import BasePage
from Base.base_page import get_locator
from app_caps import app_caps

class DeviceManagePage(BasePage):
    itemImgHeard = get_locator('Device_Manage', '设备管理')
    tvWifiSsid = get_locator('Device_Manage', '更换网络')
    rlVolumeControl = get_locator('Device_Manage', '音量控制')
    rlShowDeviceInfo = get_locator('Device_Manage', '设备信息')
    rlVersionUpdate = get_locator('Device_Manage', '升级')
    unbind = get_locator('Device_Manage', '解绑设备')
    btnNext = get_locator('Device_Manage', '开始联网')
    musicVolume = get_locator('Device_Manage', '媒体音量')
    alarmVolume = get_locator('Device_Manage', '闹钟音量')
    tvSoundBoxSoftCurrentVersion = get_locator('Device_Manage', '音箱版本')
    tvSoundBoxSystemCurrentVersion = get_locator('Device_Manage', '系统版本')
    tvDeviceModel = get_locator('Device_Manage', '音箱型号')
    tvDeviceSN = get_locator('Device_Manage', '序列号')
    tvDeviceMacAddress = get_locator('Device_Manage', 'mac地址')
    tvDeviceOSVersion = get_locator('Device_Manage', '系统版本')

    def __init__(self,driver):
        super(DeviceManagePage,self).__init__(driver)

    def enter_into_devic_manage(self):
        self.click_element(self.navigation_user)
        self.enter_into(DeviceManagePage.itemImgHeard)

    #点击切换网络，进入到配网界面
    def change_network(self):
        self.click_element(DeviceManagePage.tvWifiSsid)
        page_info = self.find_element(DeviceManagePage.btnNext).text
        return page_info

    #调节媒体音量
    def set_music_value(self):
        self.click_element(DeviceManagePage.rlVolumeControl)
        self.swipe_right(x1=0.1,y1=0.24,x2=0.5,y2=0.24)

    #调节闹钟音量
    def set_alarm_value(self):
        self.click_element(DeviceManagePage.rlVolumeControl)
        self.swipe_right(x1=0.1, y1=0.425, x2=0.5, y2=0.425)

    #设备信息
    def get_device_info(self):
        self.click_element(self.rlShowDeviceInfo)
        self.im_back()
        device_model = self.find_element(self.tvDeviceModel).text
        device_sn = self.find_element(self.tvDeviceSN).text
        mac_address = self.find_element(self.tvDeviceMacAddress)
        os_version = self.find_element(self.tvDeviceOSVersion).text
        return device_model,device_sn,mac_address,os_version

    #升级
    def update(self):
        self.click_element(self.rlVersionUpdate)
        box_current_version = self.find_element(self.tvSoundBoxSoftCurrentVersion).text
        system_current_version = self.find_element(self.tvSoundBoxSystemCurrentVersion).text
        return box_current_version,system_current_version

    def unbind_device(self):
        self.click_element(self.unbind)








if __name__ == '__main__':
    device_ob = DeviceManagePage(app_caps())
    # device_ob.set_music_value()
    device_ob.set_alarm_value()









