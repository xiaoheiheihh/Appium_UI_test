# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 11:09
# @File    : favorite_page.py
# @Software: PyCharm Community Edition

from Base.base_page import BasePage
from Pages.music_page import MusicPage
from app_caps import app_caps
import time
from Pages.tools import get_locator

class FavoritePage(MusicPage,BasePage):
    stvPlayAll = get_locator('Favorite', '播放全部')
    tvRight = get_locator('Favorite', '管理')
    tvTitle = get_locator('Favorite', '选择图标')
    btnDelete = get_locator('Favorite', '删除')
    stvAllSelect = get_locator('Favorite', '全选')
    beSure = get_locator('Favorite', '确认')
    cancel = get_locator('Favorite', '取消')
    swipe_right = get_locator('Favorite', '左滑后出来的删除图标')
    stvLike = get_locator('Favorite', '我的收藏')
    tvEmptyTip = get_locator('Favorite', '您还没有收藏任何音乐哦')

    def __init__(self,driver):
        super(FavoritePage,self).__init__(driver)

    #从我的进入到我的收藏
    def user_into_like(self):
        self.enter_into(self.navigation_user)
        self.enter_into(FavoritePage.stvLike)

    #播放音乐
    def play_music(self,singer_id,song_id):
        self.find_element(self.navigation_home).click()
        self.click_element(MusicPage.lyMusic)
        self.click_recommended_list(singer_id, song_id)
        time.sleep(8)

    #播放器界面点击收藏图标
    def collect_music(self):
        element = self.find_element(MusicPage.imFavorite)
        result = element.get_attribute('selected')
        toast_text='已收藏'
        if result == 'false':
            self.click_element(MusicPage.imFavorite)
            message = '//*[contains(@text,"收藏")]'
            toast_text = self.find_element_xpath(message).text
            time.sleep(1)
        song_info = self.find_element(FavoritePage.tvTitle).text
        favorite_status = self.find_element(self.imFavorite).get_attribute('selected')
        return song_info,favorite_status,toast_text

    #取消收藏
    def cancel_collect(self):
        self.click_element(self.imFavorite)
        message = '//*[contains(@text,"收藏")]'
        toast_text = self.find_element_xpath(message).text
        time.sleep(2)
        favorite_status = self.find_element(self.imFavorite).get_attribute('selected')
        return favorite_status,toast_text

    #收藏列表为空时，收藏多首歌曲，并回到收藏列表页
    def empty_collect_music(self):
        if self.find_element(self.tvEmptyTip):
            self.back_to_home()
            self.play_music(4, 6)
            for i in range(3):
                self.collect_music()
                self.click_element(self.btnNext)
                time.sleep(2)
            self.back_to_home()
            self.user_into_like()
        else:
            pass

    #进入收藏列表，如果有收藏的音乐时，删除收藏音乐，并返回到首页
    def enter_favorite_delete_all(self):
        self.back_to_home()
        self.user_into_like()
        if self.find_element(self.tvEmptyTip):
            pass
        else:
            self.delete_all_favorite()
        self.back_to_home()


    #从首页进入到收藏列表，如果收藏列表为空，则先收藏音乐，再回到收藏列表
    def enter_into_favorite(self):
        self.back_to_home()
        self.user_into_like()
        self.empty_collect_music()

    #播放收藏列表的歌曲
    def play_favorite_song(self,num):
        element = self.find_elements(FavoritePage.tvTitle)
        song_name = element[num].text
        element[num].click()
        return song_name

    #获取收藏列表歌曲的名称
    def get_favorite_songname(self):
        song_name = []
        if self.find_element(FavoritePage.tvTitle):
            song_list = self.find_elements(FavoritePage.tvTitle)
            song_name = []
            for i in range(len(song_list)):
                songname = song_list[i].text
                song_name.append(songname)
        else:
            song_name.append('歌曲列表为空')
        return song_name

    #获取正在播放的歌曲名称
    def get_playing_song(self):
        song = self.find_element(FavoritePage.tvTitle).text
        return song

    #删除收藏列表的第一首歌
    def delete_favorite(self):
        self.click_element(FavoritePage.tvRight)
        song_list = self.find_elements(FavoritePage.tvTitle)
        song_info = song_list[0].text
        song_list[0].click()
        self.click_element(FavoritePage.btnDelete)
        self.click_element(FavoritePage.beSure)
        return song_info

    #删除多个歌曲
    def delete_current_favorite(self):
        self.click_element(FavoritePage.tvRight)
        song_list = self.find_elements(FavoritePage.tvTitle)
        for i in range(len(song_list)):
            song_list[i].click()
        self.click_element(FavoritePage.btnDelete)
        self.click_element(FavoritePage.beSure)

    #删除所有收藏音乐
    def delete_all_favorite(self):
        if not self.find_element(self.tvEmptyTip):
            self.click_element(FavoritePage.tvRight)
            self.click_element(FavoritePage.stvAllSelect)
            self.click_element(FavoritePage.btnDelete)
            self.click_element(FavoritePage.beSure)

    #左滑删除收藏的歌曲
    def delete_favorite_swipe(self):
        song_delete = self.get_favorite_songname()[0]
        self.swipe_left()
        self.click_element(FavoritePage.swipe_right)
        self.click_element(FavoritePage.beSure)
        return song_delete

    #全选后，勾掉其中一首歌曲，全选按钮置灰
    def all_select_deselect(self):
        self.click_element(FavoritePage.tvRight)
        self.click_element(FavoritePage.stvAllSelect)
        self.find_elements(FavoritePage.tvTitle)[0].click()
        result = self.find_element(FavoritePage.stvAllSelect).get_attribute('selected')
        return result

    #播放所有歌曲
    def play_all(self):
        self.click_element(FavoritePage.stvPlayAll)


if __name__ == '__main__':
    favo = FavoritePage(app_caps())
    favo.play_favorite_song(1)