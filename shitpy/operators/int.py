from __future__ import print_function
from random import randint
import time

class int:
    def __init__(self, n):
        self.number = n

    def __add__(self, n):
        """ You want to add two numbers. 
            Why not to concatenate them? :p
        """
        print("Wait! I am Pooping...")
        print("Initializing Pooping Sequence")
        
        for i in range(3):
            print(".",end=" ")
            time.sleep(1)
        
        t = randint(2, 6)
        
        for i in range(t):
            print("""
                      ^
                    (___)
                   (_____)""")
            time.sleep(1)
        
        a = str(self.number)
        b = str(n.number)        
        c = a + b
        print("Aaahhhh!! Feels so Good!")
        
        return int(c)

    def __repr__(self):
        return str(self.number)
        
    def __str__(self):
        return str(self.number)
