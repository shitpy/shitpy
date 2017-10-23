from __future__ import print_function
from random import randint
import time

class int:
    def __init__(self, n):
        self.number = n

    def make_turd(self, levels):
        '''
            Creates a pile of shit levels high.
        '''

        turd = levels * ' ' + '^'

        for i in range(2, levels + 1):
            turd += ('\n' + (levels - i)* ' ' + '(' + (2*i - 1) *'_' + ')')

        return turd

    def __add__(self, n):
        """ You want to add two numbers. 
            Why not to concatenate them? :p
        """
        print("Wait! I am Pooping...")
        
        t = randint(1, 6)
        
        if t == 1:
            time.sleep(1)
            print(self.make_turd(4) + 

            """Aahhh! AAAHHH! Its huge!""")
            time.sleep(2)
            print("FEELS SO GOOD!")
        else:
            for i in range(t):
                print(self.make_turd(3))
                time.sleep(1)
            print("Aaahhhh!! Feels so Good!")
        
        a = str(self.number)
        b = str(n.number)        
        c = a + b
        
        return int(c)

    def __mul__(self, n):
        """ You want to multiply two numbers.
        """
        print("Wait! I am Pooping...")

        t = randint(1, 6)

        if t == 1:
            time.sleep(1)
            print(self.make_turd(5) + 
                """

            Aahhh! AAAHHH! Its huge!
                 Its bigger!
                 Its badder!
            Its the biggest shit ever""")
            time.sleep(2)
            print("FEELS SO GOOD!")
        else:
            for i in range(t):
                print(self.make_turd(3))
                time.sleep(1)
            print("Aaahhhh!! Feels so Good!")

        a = str(self.number)
        b = n.number
        c = a * b

        return int(c)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __repr__(self):
        return str(self.number)
        
    def __str__(self):
        return str(self.number)
