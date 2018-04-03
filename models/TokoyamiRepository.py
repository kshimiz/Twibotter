# coding:utf-8

from pprint import pprint
from datetime import datetime

import tweepy as tp

class TokoyamiRepository:

    """ TokoyamiRepositoryリポジトリクラス """

    def __init__(self):
        #基準日
        self.ORG_DATE = '2018-4-1'
        #基準日の強さ(-1)
        self.BOSS_MST = {
            'レグナード' : 0,
            'ダークキング' : 2,
            'メイヴ' : 1,
        }

    #tweetするテキストを取得する
    def text(self):
        result = ''
        tday = datetime.now()
        result += '【bot】今日(' + tday.strftime("%Y/%m/%d") + ')の常闇ボスは...\n'
        for name, level in self.BOSS_MST.items():
            oday = datetime.strptime(str(self.ORG_DATE), "%Y-%m-%d")
            d = (tday-oday).days
            result += name + ':' + str((level+d)%4+1) + '\n'
        return result

    #削除対象tweet検索用の文字列を取得する
    def delkey(self):
        return '【bot】今日'
