# coding:utf-8

import os
import json
from pprint import pprint
from datetime import datetime

from lib.TwitterWrapper import TwitterWrapper
from models.TokoyamiRepository import TokoyamiRepository

class Controller:

    """ Controllerクラス """

    def __init__(self):
        pass

    #
    # dqx:今日の常闇ボスの強さをtweetする
    #
    def tokoyami(self):

        print(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ":tokoyami-start")

        # Twitter認証キーを取得
        with open(os.path.dirname(__file__) + "/../conf/secret.json") as f:
            secretjson = json.load(f)
        t = TwitterWrapper(secretjson);

        # モデルを取得
        model = TokoyamiRepository()

        # 古いtweetを削除
        t.mytweet_del(model.delkey())

        # テキスト作成
        text = model.text()

        # tweetする
        t.tweet(text)

        print(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ":tokoyami-end")
