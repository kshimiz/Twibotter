# coding:utf-8

import sys

class Argument:

    """ 引数クラス """

    def __init__(self):
        self.argc = len(sys.argv)
        self.argvs = sys.argv

    def getTarget(self):
        return self.argvs[1]


