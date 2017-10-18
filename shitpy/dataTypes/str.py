from random import random

class str:
    def __init__(self, s):
        self.string = s

    def __add__(self, x):
        print("Life Is Not Always What We Want It To Be (o_o)")
        try:
            a = int(self.string)
            b = int(x)
            c = a + b
            return c
        except:
            print("Wtf is this! I can't add it!")
            print("I'll give you a good one!")
            return int(random() * 100)

    def __str__(self):
        return self.string
