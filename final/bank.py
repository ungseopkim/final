# -*- coding: utf-8 -*-

class account:    
    def __init__(self, number):
        self.number = number
        
class parents(account):
    def __init__(self, number, name, money):
        account.__init__(self, number, name, money)
        self.number       
        self.money
        
class children(parents):
    def __init__(self, number, name, parents):
        parents.__init__(self, number, name, parents)
        self.parents = parents
        self.name = name        
        self.number = number


