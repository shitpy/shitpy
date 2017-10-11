class int:
    def __init__(self, n):
        self.number = n

    def __add__(self, n):
        """ You want to add two numbers. 
            Why not to concatenate them? :) 
        """
        print("Pooping CPU... ", end='')
        a = str(self.number)
        b = str(n)        
        c = a + b
        print("Done")
        return c

    def __str__(self):
        return str(self.number)
