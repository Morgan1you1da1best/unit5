#Morgan Baughman
#11/17/17
#betterColorChangeWindow.py

from random import randint
from ggame import *

def mouseClick(event):
    colorList=['0xFF0000','0x0000FF','0x00FF00','0xE033FF','0x33FF8D']
    color = Color(colorList[randint(1,5)-1], 1)
    colorRectangle = RectangleAsset(1000, 1000, LineStyle(1, color), color)



    Sprite(colorRectangle)
App().listenMouseEvent("click", mouseClick)
App().run()

