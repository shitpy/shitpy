from random import random
import time

class str:
    '''
    >>> from shitpy import str
    >>> str(4) + str('abc')
    Life is not always what we want it to be (o_o)
    Wtf is this! I can't add it!
    But wait! I'll give you some random shit!
    12.9651505349 #some random number

    >>> str(45) + str(78)
    Life is not always what we want it to be (o_o)
    Computing some Shit!
    123
    '''
    def __init__(self, s):
        self.string = s

    def __add__(self, x):
        print("Life is not always what we want it to be (o_o)")
        time.sleep(2)
        a = self.string
        b = x.string
        try:
            a = int(a)
            b = int(b)
            print("Computing some Shit!")
            c = a + b
            time.sleep(2)
            return str(c)
        except:
            print("Wtf is this! I can't add it!")
            time.sleep(2)
            print("But wait! I'll give you some random shit!")
            time.sleep(2)
            return str(random() * 100)

    def __str__(self):
        return "%s"%self.string
        
    def __repr__(self):
        return "%s"%self.string