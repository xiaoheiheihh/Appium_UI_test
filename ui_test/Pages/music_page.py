# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 17:07
# @File    : music_page.py
# @Software: PyCharm Community Edition

from Base.base_page import BasePage
import app_caps
import time
from Pages.tools import get_locator


class MusicPage(BasePage):
    lyMusic= get_locator('Music','音乐')
    imgSingerHeard = get_locator('Music', '推荐的歌手')
    tv_commend_more = get_locator('Music', '推荐歌曲_更多')
    rightImage = get_locator('Music', '播放器')
    tvMusicSingerSizes = get_locator('Music', '歌曲数量')
    imgSingerItemTitle = get_locator('Music', '播放列表的歌曲名称')
    imFavorite = get_locator('Music', '收藏图标')
    tvTitle = get_locator('Music', '正在播放的歌曲名称')
    tvArtist = get_locator('Music', '歌手信息')
    btnPlay = get_locator('Music', '播放/暂停按钮')
    imgPlay = get_locator('Music', '播放全部')
    tvName = get_locator('Music', '推荐歌曲列表')
    btnPrev = get_locator('Music', '上一首歌')
    btnNext = get_locator('Music', '下一首歌')
    btnPlayMode = get_locator('Music', '播放模式')
    btnCurrentList = get_locator('Music', '播放列表图标')
    tvSongNameContent = get_locator('Music','推荐歌曲的歌名')

    def __init__(self,driver):
        super(MusicPage, self).__init__(driver)

    #进入到音乐界面
    def enter_into_music(self):
        self.enter_into(MusicPage.lyMusic)

    #获取音乐播放器界面，歌曲的名称
    def get_song_info(self):
        return self.find_element(MusicPage.tvTitle).text

    #获取推荐的歌手，返回歌手列表
    def get_recommended_list(self):
        recommended_singer = self.find_elements(MusicPage.imgSingerHeard)
        return recommended_singer

    #获取每个推荐歌手列表的歌曲
    def get_songs(self):
        recommended_singer_songs=self.find_elements(MusicPage.imgSingerItemTitle)
        return recommended_singer_songs

    #播放推荐歌手的歌曲，参数为：歌手和歌曲的索引号
    def click_recommended_list(self,singer,song):
        # self.enter_into(MusicPage.music)
        recommended_list = self.get_recommended_list()
        recommended_list[singer].click()
        recommended_singer_songs = self.get_songs()
        recommended_singer_songs[song].click()

    #播放首页推荐的歌曲
    def click_recommended_songs(self,num):
        self.enter_into(MusicPage.lyMusic)
        recommended_singer = self.get_recommended_list()
        recommended_singer[num].click()

    #循环播放推荐歌曲的歌曲
    def play_recommended_singers(self):
        self.enter_into(MusicPage.lyMusic)
        #歌曲名称列表
        song_name_list = []
        #播放的歌曲名称列表
        played_song_name_list = []
        # singer_len = len(singers)
        for i in range(6):
            singers = self.find_elements(MusicPage.imgSingerHeard)
            singers[i].click()
            time.sleep(2)
            songs= self.get_songs()
            # for j in range(len(songs)):
            for j in range(8):
                song_title = self.find_elements(MusicPage.imgSingerItemTitle)
                song_name_list.append(song_title[j].text)
                time.sleep(1)
                song_title[j].click()
                time.sleep(8)
                played_song_name_list.append(self.find_element(MusicPage.tvTitle).text)
                time.sleep(1)
                self.im_back()
                time.sleep(1)
            self.im_back()
            time.sleep(1)
        return song_name_list,played_song_name_list

    #播放推荐的6首歌曲
    def play_recommended_songs(self):
        self.enter_into(MusicPage.lyMusic)
        self.swipe_up()
        song_name_list = []
        played_song_name_list = []
        for i in range(6,12):
            recommended_songs = self.find_elements(MusicPage.tvSongNameContent)
            song_name_list.append(recommended_songs[(i-6)].text)
            recommended_songs[(i-6)].click()
            time.sleep(8)
            played_song_name_list.append(self.find_element(MusicPage.tvTitle).text)
            time.sleep(2)
            self.im_back()
            time.sleep(1)
        return song_name_list, played_song_name_list

    #播放更多的收藏歌曲---播放全部
    def play_all_recommended_songs(self):
        self.enter_into(MusicPage.lyMusic)
        self.click_element(MusicPage.tv_commend_more)
        song_name = self.find_elements(MusicPage.tvName)[0].text
        self.click_element(MusicPage.imgPlay)
        time.sleep(5)
        played_song_name = self.find_element(MusicPage.tvTitle).text
        return song_name, played_song_name

    #播放更多的推荐歌曲
    def play_more_recommended_songs(self):
        self.enter_into(MusicPage.lyMusic)
        self.click_element(MusicPage.tv_commend_more)
        song_name_list = []
        played_song_name_list = []
        song_name = self.find_elements(MusicPage.tvName)
        for i in range(len(song_name)):
            song_name = self.find_elements(MusicPage.tvName)
            song_name_list.append(song_name[i].text)
            song_name[i].click()
            time.sleep(8)
            played_song_name_list.append(self.find_element(MusicPage.tvTitle).text)
            time.sleep(1)
            self.im_back()
            time.sleep(1)
        return song_name_list,played_song_name_list

    #切换播放模式,并切换下一首歌---循环/顺序/单曲
    def change_playmode(self,i,j):
        self.enter_into(MusicPage.lyMusic)
        song_name_list = []
        singers = self.find_elements(MusicPage.imgSingerHeard)
        singers[i].click()
        song_title = self.find_elements(MusicPage.imgSingerItemTitle)
        for m in range(len(song_title)):
            song_name_list.append(song_title[m].text)
        next_song = song_name_list[(j + 1)]
        song_title[j].click()
        time.sleep(8)
        self.click_element(MusicPage.btnPlayMode)
        time.sleep(2)
        self.click_element(MusicPage.btnNext)
        time.sleep(10)
        played_song_name = self.find_element(MusicPage.tvTitle).text
        return next_song,played_song_name

    #暂停播歌时，点击下一首
    def pause_next(self,i,j):
        self.enter_into(MusicPage.lyMusic)
        song_name_list = []
        singers = self.find_elements(MusicPage.imgSingerHeard)
        singers[i].click()
        song_title = self.find_elements(MusicPage.imgSingerItemTitle)
        for m in range(len(song_title)):
            song_name_list.append(song_title[m].text)
        next_song = song_name_list[(j + 1)]
        song_title[j].click()
        time.sleep(10)
        self.click_play_mode()
        self.click_play_pause()
        time.sleep(1)
        self.click_element(self.btnNext)
        time.sleep(10)
        played_song_name = self.find_element(MusicPage.tvTitle).text
        return next_song, played_song_name

    #拉取播放列表
    def swipe_song_list(self):
        self.enter_into(MusicPage.lyMusic)
        singers = self.find_elements(MusicPage.imgSingerHeard)
        singers[0].click()
        for i in range(20):
            self.swipe_up(y2=0.1)
        time.sleep(10)

    #播放约第150首歌
    def play_more_songs(self):
        self.swipe_song_list()
        song_length = self.find_element(MusicPage.tvMusicSingerSizes).text
        song_name_list = []
        song_title = self.find_elements(MusicPage.imgSingerItemTitle)
        for m in range(len(song_title)):
            song_name_list.append(song_title[m].text)
        song_title[0].click()
        time.sleep(10)
        # print('当前歌曲长度是:',song_length)
        played_song_name = self.find_element(MusicPage.tvTitle).text
        return song_name_list[0],played_song_name

    #点击播放模式按钮
    def click_play_mode(self):
        self.click_element(MusicPage.btnPlayMode)

    #切换播放/暂停
    def change_play_pause(self):
        self.enter_into(MusicPage.lyMusic)
        songs = self.find_elements(MusicPage.tvSongNameContent)
        songs[1].click()
        time.sleep(10)
        self.click_element(MusicPage.btnPlay)

    #点击播放暂停按钮
    def click_play_pause(self):
        self.click_element(MusicPage.btnPlay)

if __name__ == '__main__':
    music_ob = MusicPage(app_caps.app_caps())
    # music_ob.click_recommeded_list(2,3)
    # music_ob.clikc_recommended_songs(-1)
    # music_ob.play_recommended_songs()
    # music_ob.play_recommended_singers()
    # music_ob.play_more_recommended_songs()
    # music_ob.play_more_recommended_songs()
    # music_ob.change_playmode(0,0)
    # music_ob.swipe_song_list()
    music_ob.play_more_songs()

