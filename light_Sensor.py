from microbit import *
from time import *
brightness= 0
controlBrightness= 0
positionControl= 0
x_position = 0
y_position = 0
while True:
    
    controlBrightness= (display.read_light_level() // 10) * 10 
    brightness = display.read_light_level() - controlBrightness
    positionControl = display.read_light_level() // 50
    y_position = 4 - positionControl
    x_position = (display.read_light_level()-(positionControl*50))// 10


    for i in range(5):
        if(i > y_position):
            for j in range(5):
                display.set_pixel(j,i,9)

        if(i < y_position):
            for j in range(5):
                display.set_pixel(j,i,0)
                
        if i == y_position:
            for j in range(5):
                if(j < x_position):
                    display.set_pixel(j,i,9)

                if(j > x_position):
                    display.set_pixel(j,i,0)
               
                


    if (y_position < 0):
        display.set_pixel(4,0, 9)
    else:
        display.set_pixel(x_position, y_position, brightness)

    