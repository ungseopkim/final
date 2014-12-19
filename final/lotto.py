# -*- coding: utf-8 -*-

import random

class LottoBall:
    def __init__(self, num):
        self.num = num

class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))
    def selectBalls(self):
        random.shuffle(self.ballList)
        return self.ballList[0:6]
        
class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()
    def playLotto(self):
        pass

if __name__=='__main__':
    ui = LottoUI()
    ui.playLotto()


ballList = range(1,46)
random.shuffle(ballList)
print sorted(ballList[0:6])