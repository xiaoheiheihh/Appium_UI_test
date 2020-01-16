# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 14:11
# @File    : test_6device_manage.py
# @Software: PyCharm Community Edition

from Pages.device_manage_page import DeviceManagePage
from Base.public import create_screenshot
import unittest
import app_caps

class DeviceManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = app_caps.app_caps()
        cls.device_manage = DeviceManagePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_device_management_001(self):
        """进入到设备管理页面"""
        self.device_manage.enter_into_devic_manage()
        self.driver.get_screenshot_as_file(create_screenshot('设备管理')+'/设备管理页面.jpg')

    def test_device_management_002(self):
        """点击更换网络，进入到联网界面"""
        page_info = self.device_manage.change_network()
        self.assertEqual(page_info,'橙色灯光已亮起，开始联网')
        self.device_manage.click_element(('id','com.unisound.unione.phone:id/btnBack'))

    def test_device_management_003(self):
        """调节媒体音量"""
        self.device_manage.set_music_value()
        self.driver.get_screenshot_as_file(create_screenshot('设备管理')+'/媒体音量.jpg')
        self.device_manage.im_back()

    def test_device_management_004(self):
        """调节媒体音量"""
        self.device_manage.set_alarm_value()
        self.driver.get_screenshot_as_file(create_screenshot('设备管理')+'/闹钟音量.jpg')
        self.device_manage.im_back()

    # def test_device_management_005(self):
    #     """检查设备信息"""
    #     device_model, device_sn, mac_address, os_version = self.device_manage.get_device_info()
    #     self.driver.get_screenshot_as_file(create_screenshot('设备管理')+'/设备信息.jpg')
    #     self.assertEqual(device_model,'Unione音箱')
    #     self.assertEqual(device_sn, 'Test_SN_1234567')
    #     self.assertEqual(mac_address, 'ac-5d-5c-03-fa-53')
    #     self.assertEqual(device_model, 'v1.0.0')
    #     self.device_manage.im_back()

    def test_device_management_006(self):
        """检查升级界面版本信息"""
        box_current_version, system_current_version = self.device_manage.update()
        self.assertEqual(box_current_version,'版本: v2.2.13-2692-2019091815')
        self.assertEqual(system_current_version,'v1.0.0')
        self.device_manage.im_back()

    def test_device_management_007(self):
        """解绑设备时，点击取消"""
        self.device_manage.unbind_device()
        self.device_manage.popup_cancel()
        self.assertTrue(self.device_manage.find_element(self.device_manage.unbind))

    # def test_device_management_008(self):
    #     """解绑设备时，点击确定"""
    #     self.device_manage.unbind_device()
    #     self.device_manage.popup_cancel()
    #     self.assertTrue(self.device_manage.find_element(self.device_manage.itemImgHeard))

if __name__ == '__main__':
    unittest.main(verbosity=2)






