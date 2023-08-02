import random
class RandomColor:

    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.color = ()
        
    def generate_color(self):
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.color = (self.r,self.g,self.b)
        return self.color