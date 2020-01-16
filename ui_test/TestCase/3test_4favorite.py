# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:46
# @File    : test_4favorite.py
# @Software: PyCharm Community Edition

import unittest
import app_caps
from Pages.favorite_page import FavoritePage
import time


class Favorite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = app_caps.app_caps()
        cls.favorite = FavoritePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_favorite_001(self):
        """没有收藏音乐时，界面提示语检测"""
        self.favorite.user_into_like()
        self.favorite.delete_all_favorite()
        empty = self.favorite.find_element(self.favorite.tvEmptyTip).text
        self.assertEqual(empty,'你还没有收藏任何音乐哦')

    def test_favorite_002(self):
        """没有收藏音乐时，收藏一首歌曲"""
        time.sleep(1)
        self.favorite.back_to_home()
        self.favorite.play_music(2,6)
        song_info,_status,toast_text = self.favorite.collect_music()
        self.favorite.back_to_home()
        self.favorite.user_into_like()
        collect_song_info = self.favorite.get_favorite_songname()[0]
        self.assertEqual(song_info,collect_song_info)
        self.assertEqual(toast_text,'已收藏')

    def test_favorite_003(self):
        """播放音乐时，收藏音乐"""
        self.favorite.back_to_home()
        self.favorite.play_music(2,5)
        _song,favorite_status,toast_text = self.favorite.collect_music()
        self.assertEqual(favorite_status,'true')
        self.assertEqual(toast_text,'已收藏')

    def test_favorite_004(self):
        """暂停播放音乐时，收藏音乐"""
        self.favorite.back_to_home()
        self.favorite.play_music(4,4)
        self.favorite.click_element(self.favorite.btnPlay)
        _song,favorite_status,toast_text = self.favorite.collect_music()
        self.assertEqual(favorite_status,'true')
        self.assertEqual(toast_text,'已收藏')

    def test_favorite_005(self):
        """播放收藏的音乐时，取消收藏"""
        self.favorite.enter_into_favorite()
        self.favorite.play_favorite_song(0)
        favorite_status,toast_text = self.favorite.cancel_collect()
        time.sleep(2)
        self.assertEqual(favorite_status,'false')
        self.assertEqual(toast_text,'收藏已取消')

    def test_favorite_006(self):
        """暂停播放收藏音乐时，取消收藏"""
        self.favorite.enter_into_favorite()
        self.favorite.play_favorite_song(0)
        self.favorite.click_play_pause()
        favorite_status,toast_text = self.favorite.cancel_collect()
        time.sleep(2)
        self.assertEqual(favorite_status,'false')
        self.assertEqual(toast_text,'收藏已取消')

    def test_favorite_007(self):
        """验证收藏顺序，最新收藏的显示在最上方"""
        time.sleep(1)
        self.favorite.back_to_home()
        self.favorite.user_into_like()
        self.favorite.delete_all_favorite()
        self.favorite.back_to_home()
        self.favorite.play_music(2,6)
        song_info_list = []
        for i in range(3):
            song_info,_status,toast_text = self.favorite.collect_music()
            song_info_list.append(song_info)
            time.sleep(1)
            self.favorite.click_element(self.favorite.btnNext)
            time.sleep(3)
        self.favorite.back_to_home()
        self.favorite.user_into_like()
        song_info_current= self.favorite.get_favorite_songname()
        self.assertEqual(song_info_list,list(reversed(song_info_current)))

    def test_favorite_008(self):
        """播放我的收藏里的全部歌曲"""
        self.favorite.enter_into_favorite()
        song = self.favorite.get_favorite_songname()
        self.favorite.play_all()
        song_play = self.favorite.get_playing_song()
        self.assertEqual(song[0], song_play)
        for i in range(3):
            self.favorite.click_element(self.favorite.btnNext)
            self.assertEqual(self.favorite.find_element(self.favorite.imFavorite).get_attribute('selected'),'true')

    # def test_favorite_009(self):
    #     """收藏超过200首歌曲"""
    #     self.favorite.back_to_home()
    #     self.favorite.user_into_like()
    #     self.favorite.delete_all_favorite()
    #     self.favorite.back_to_home()
    #     self.favorite.play_music(2, 6)
    #     song_info_list = []
    #     for i in range(200):
    #         song_info, _status,toast_text = self.favorite.collect_music()
    #         song_info_list.append(song_info)
    #         time.sleep(1)
    #         self.favorite.click_element(self.favorite.btnNext)
    #         time.sleep(3)
    #     print('歌曲列表的长度是:',len(song_info_list))
    #     self.assertEqual(len(song_info_list),200)

    def test_favorite_010(self):
        """从收藏列表删除一首歌曲"""
        self.favorite.enter_into_favorite()
        song_delete = self.favorite.delete_favorite()
        song = self.favorite.get_favorite_songname()[0]
        print(song)
        self.assertNotEqual(song,song_delete)

    def test_favorite_011(self):
        """从收藏列表里删除多个歌曲"""
        self.favorite.enter_into_favorite()
        song_delete = self.favorite.delete_current_favorite()
        song = self.favorite.get_favorite_songname()[0]
        self.assertNotEqual(song_delete,song)

    def test_favorite_012(self):
        """删除所有收藏的歌曲"""
        self.favorite.enter_into_favorite()
        self.favorite.delete_all_favorite()
        empty = self.favorite.find_element(self.favorite.tvEmptyTip).text
        self.assertEqual(empty,'你还没有收藏任何音乐哦')

    def test_favorite_013(self):
        """左滑删除收藏的音乐"""
        self.favorite.enter_into_favorite()
        song_delete = self.favorite.delete_favorite_swipe()
        song = self.favorite.get_favorite_songname()[0]
        print('删除的歌曲是:',song_delete)
        print('当前第一首歌曲是:',song)
        self.assertNotEqual(song_delete,song)

    def test_favorite_014(self):
        """全选后，勾掉其中一首歌曲，全选按钮置灰"""
        self.favorite.enter_into_favorite()
        result = self.favorite.all_select_deselect()
        self.assertEqual(result,'false')

if __name__ == '__main__':
    unittest.main(verbosity=2)


