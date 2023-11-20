from ast import operator
from semanticCube import *
from collections import defaultdict

class PiinkkLoader():
    def __init__(self):
        self.operatorStack = []
        self.typeStack = []
        self.operandStack = []
        self.jumpStack = []
        self.dirFun = defaultdict(lambda:{'variables':{}})
        defaultdict()

    def printDir(self):
        print(self.dirFun())


piinkkLoader = PiinkkLoader()