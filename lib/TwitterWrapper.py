# coding:utf-8

import os
import sys
import re
from datetime import datetime
from datetime import timedelta
from pprint import pprint
import tweepy as tp
import json

class TwitterWrapper:

    """ Twitterラッパークラス """

    def __init__(self, secretjson):
        self.secretjson = secretjson
        self.oauth()

    #TwitterAPI認証を行う
    def oauth(self):
        auth = tp.OAuthHandler(self.secretjson["consumer_key"], self.secretjson["consumer_secret"])
        auth.set_access_token(self.secretjson["access_token"], self.secretjson["access_token_secret"])
        self.t = tp.API(auth_handler = auth, api_root ='/1.1')
        self.myid = self.t.me().id_str
        self.myscreen_name = self.t.me().screen_name

    #検索したツイート一覧を、IDで取得する
    def searchIds(self, query, language="ja", r_type="recent", cnt=100):
        result = []
        tweets = self.search(query, language, r_type, cnt)
        for status in tweets:
            result.append(status.id)
        return result

    #ツイートを検索する
    def search(self, query, language="ja", r_type="recent", cnt=100):
        return self.t.search(q=query, lang=language, count=cnt, recent_type=r_type)

    #指定した正規表現にマッチするツイートを取得する
    def search_reg(self, query, reg, language="ja", r_type="recent", cnt=100):
        result = [] 
        targets = self.search(query, language, r_type, cnt)
        for target in targets:
            match_ob = re.findall(reg, target.text)
            if match_ob:
                result.append(target)
            else:
                continue
        return result

    #指定ツイートをリツイートしたユーザー一覧を、IDで取得する
    def retweetsIds(self, rid, cnt=100):
        result = []
        twitter = self.retweets(rid, cnt)
        for status in twitter:
            result.append(status.author.screen_name)
        return result

    #指定したツイートの、RTツイート一覧をオブジェクトで取得する
    def retweets(self, rid, cnt=100):
        return self.t.retweets(rid, cnt)

    #ツイートIDを指定して、そのIDをリツイートする
    def retweet(self, rid):
        return self.t.retweet(rid)

    #ツイートする
    def tweet(self, text):
        self.t.update_status(status=text)

    #指定したtextを含むツイートを削除する
    def mytweet_del(self, serchtext):
        tl = self.t.user_timeline(id=self.myid,count=100)
        for i in tl:
            if i.text.find(serchtext) >= 0:
                self.t.destroy_status(i.id)

    #指定したtextを含むツイートを削除する
    def mytweet_search(self, serchtext):
        result = []
        tl = self.t.user_timeline(id=self.myid,count=10)
        for i in tl:
            if i.text.find(serchtext) >= 0:
                result.append(i)
        return result

    #未返信の自分宛ツイートを取得する
    def get_timeline_noreply(self, minutes):
        result = []
        now = datetime.now()
        ago = now - timedelta(minutes=minutes)
        timeline=self.t.mentions_timeline()
        for status in timeline:
            localtime = status.created_at + timedelta(hours=9)
            if localtime > ago:
                result.append(status)
        return result

    #返信する
    def reply(self, text, target_id):
        self.t.update_status(status=text,in_reply_to_status_id=target_id)
