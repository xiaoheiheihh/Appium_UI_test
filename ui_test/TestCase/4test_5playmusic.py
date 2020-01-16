# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 17:34
# @File    : test_5playmusic.py
# @Software: PyCharm Community Edition

import unittest
import app_caps
from Pages.music_page import MusicPage
from Base.public import create_screenshot
import time


class Music(unittest.TestCase):
    # path = os.path.basename(os.path.dirname('.'))

    @classmethod
    def setUpClass(cls):
        cls.driver = app_caps.app_caps()
        cls.music = MusicPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_music_001(self):
    #     """循环播放推荐歌手的歌曲"""
    #     singer_songs, played_singer_songs = self.music.play_recommended_singers()
    #     self.assertEqual(singer_songs,played_singer_songs)

    # def test_music_002(self):
    #     """播放推荐的6首歌曲"""
    #     self.music.back_to_home()
    #     singer_songs, played_singer_songs = self.music.play_recommended_songs()
    #     self.assertEqual(singer_songs,played_singer_songs)

    def test_music_003(self):
        """播放全部时播放的是列表的第一首歌"""
        self.music.back_to_home()
        singer_songs, played_singer_songs = self.music.play_all_recommended_songs()
        self.assertEqual(singer_songs,played_singer_songs)

    def test_music_004(self):
        """播放更多的推荐歌曲"""
        self.music.back_to_home()
        singer_songs, played_singer_songs = self.music.play_more_recommended_songs()
        self.assertEqual(singer_songs,played_singer_songs)

    def test_music_005(self):
        """切换播放模式为顺序播放，循环播放到顺序播放"""
        self.music.back_to_home()
        singer_songs, played_singer_songs = self.music.change_playmode(0,0,)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/顺序播放.jpg')
        self.assertEqual(singer_songs,played_singer_songs)

    def test_music_006(self):
        """切换播放模式为随机播放，顺序播放到随机播放"""
        self.music.back_to_home()
        singer_songs, played_singer_songs = self.music.change_playmode(0,0,)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/随机播放.jpg')
        self.assertNotEqual(singer_songs,played_singer_songs)

    def test_music_007(self):
        """切换播放模式为单曲循环，随机播放到单曲循环"""
        self.music.back_to_home()
        singer_songs, played_singer_songs = self.music.change_playmode(0,0,)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/单曲循环.jpg')
        self.assertEqual(singer_songs,played_singer_songs)

    def test_music_008(self):
        """切换播放模式为循环播放，单曲循环到循环播放"""
        self.music.back_to_home()
        singer_songs, played_singer_songs = self.music.change_playmode(0,0,)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/循环播放.jpg')
        self.assertEqual(singer_songs,played_singer_songs)

    def test_music_009(self):
        """切换播放状态为播放"""
        self.music.back_to_home()
        self.music.change_play_pause()
        time.sleep(1)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/暂停播放.jpg')

    def test_music_010(self):
        """切换播放状态为暂停"""
        self.music.back_to_home()
        self.music.change_play_pause()
        self.music.click_play_pause()
        time.sleep(2)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/继续播放.jpg')

    def test_music_011(self):
        """顺序播放模式下，暂停播放时，点击下一首歌，切换到下一首歌，并且播放"""
        self.music.back_to_home()
        song_name,played_song_name = self.music.pause_next(1,1)
        time.sleep(1)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/顺序播放模式下，暂停后切换下一首歌开始播放.jpg')
        self.assertEqual(song_name,played_song_name)

    def test_music_012(self):
        """随机循环模式下，暂停播放时，点击下一首歌，切换到下一首歌，并且播放"""
        self.music.back_to_home()
        song_name,played_song_name = self.music.pause_next(1,1)
        time.sleep(1)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/随机播放模式下，暂停后切换下一首歌开始播放.jpg')
        self.assertNotEqual(song_name,played_song_name)

    def test_music_013(self):
        """单曲循环模式下，暂停播放时，点击下一首歌，切换到下一首歌，并且播放"""
        self.music.back_to_home()
        song_name,played_song_name = self.music.pause_next(1,1)
        time.sleep(1)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/单曲循环模式下，暂停后切换下一首歌开始播放.jpg')
        self.assertEqual(song_name,played_song_name)

    def test_music_014(self):
        """循环播放模式下，暂停播放时，点击下一首歌，切换到下一首歌，并且播放"""
        self.music.back_to_home()
        song_name,played_song_name = self.music.pause_next(1,1)
        time.sleep(1)
        self.driver.get_screenshot_as_file(create_screenshot('music')+'/循环播放模式下，暂停后切换下一首歌开始播放.jpg')
        self.assertEqual(song_name,played_song_name)

    def test_music_015(self):
        """拉取后续列表，播放约第150首歌"""
        self.music.back_to_home()
        song_name,played_song_name = self.music.play_more_songs()
        self.assertEqual(song_name,played_song_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
