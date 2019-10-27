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

        turd = (levels * ' ' + (' '*10) + '^')

        for i in range(2, levels + 1):
            turd += '\n' + ((levels - i)*' ') + (' '*10) + '(' + (2*i - 1) *'_' + ')'

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

            """\nAahhh! AAAHHH! Its huge!""")
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

    def __sub__(self, n):

        """ You want to subtract two numbers.
            Why not do this digit by digit and concat? :p
        """
        print("Wait! I am Pooping...")

        t = randint(1, 6)

        if t == 1:
            time.sleep(1)
            print("""
                      ^
                    (___)
                   (_____)
                  (_______)
                 (_________)

            Aahhh! AAAHHH! Its huge!
                 Its bigger!
                 Its badder!
            Its the biggest shit ever""")
            time.sleep(2)
            print("FEELS SO GOOD!")
        else:
            for i in range(t):
                print("""
                          ^
                        (___)
                       (_____)""")
                time.sleep(1)
            print("Aaahhhh!! Feels so Good!")

        a = [float(num) for num in list(str(self.number)) if num is not "-"]
        b = [float(num) for num in list(str(n.number)) if num is not "-"]
        if len(a) > len(b):
            while(len(a) > len(b)):
                b.append(0)
        elif len(b) > len(a):
            while(len(b) > len(a)):
                a.append(0)
        c = ""
        for n in range(len(a)):
            c = c + str(a[n] - b[n])

        return c + " is the One trUe shiT Answer"

    def __rmul__(self, n):
        return self.__mul__(n)

    def __repr__(self):
        return str(self.number)

    def __str__(self):
        return str(self.number)