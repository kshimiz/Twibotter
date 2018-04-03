# coding:utf-8

from lib.Argument import Argument
from controllers.Controller import Controller

class Application:

    """ 起動アプリケーションクラス """

    def __init__(self):
        #コマンド引数
        self.argument = Argument()
        #コントローラ
        self.ctrl = Controller()

    def run(self):
        target = self.argument.getTarget()

        #引数により実行メソッドを切り替え
        if target == "tokoyami":
            self.ctrl.tokoyami()
        else:
            pass
