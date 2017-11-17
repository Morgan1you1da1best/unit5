#Morgan Baughman
#11/17/17
#betterColorChangeWindow.py


from random import randint
from ggame import *


blue = Color(0x0000FF, 1)
red = Color(0xFF0000, 1)
green = Color(0x00FF00, 1)
lightgreen = Color(0x33FF8D, 1)
purple = Color(0xE033FF, 1)


def mouseClick(event):
    num = randint(1,4)
    
redRectangle = RectangleAsset(700, 700, LineStyle(1, red), red)
lightgreenRectangle = RectangleAsset(700, 700, LineStyle(1, lightgreen), lightgreen)
greenRectangle = RectangleAsset(700, 700, LineStyle(1, green), green)
purpleRectangle = RectangleAsset(700, 700, LineStyle(1, purple), purple)
blueRectangle = RectangleAsset(700, 700, LineStyle(1, blue), blue)

Sprite(redRectangle)
Sprite(blueRectangle)
Sprite(lightgreenRectangle)
Sprite(greenRectangle)
Sprite(purpleRectangle)


App().listenMouseEvent("click", mouseClick)
App().run()

