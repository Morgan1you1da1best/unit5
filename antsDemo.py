#Morgan Baughman
#11/20/17
#antsDemo.py - how to use lists with graphics

from ggame import*
from random import randint

WIDTH = 800
HEIGHT = 400

if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(4,LineStyle(1,red),red)
    
    for i in range(100):
        Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT)))
    
    App().run()