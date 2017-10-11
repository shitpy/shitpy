from random import randint
import time

class int:
    def __init__(self, n):
        self.number = n

    def __add__(self, n):
        """ You want to add two numbers. 
            Why not to concatenate them? :) 
        """

        print("Pooping CPU... ")
        print("Pooping takes time, I am so Shitty...")
        t = randint(2, 6)
        time.sleep(t)
        a = str(self.number)
        b = str(n.number)        
        c = a + b
        print("Aaahhhh!! Feels so Good!")
        return c

    def __str__(self):
        return str(self.number)
