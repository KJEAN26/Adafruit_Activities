"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library

from adafruit_circuitplayground import cp
from time import sleep
cp.pixels.brightness = 1


color = 0
ndx = 0
temp = 0
i = 0
while True:
    
    ndx = cp.light // 32 
    num = (cp.light // 32) * 32
    
    i = i if i < 10 else 0

    
    
    if i == ndx:
        color = int(255*(cp.light-num)/32)        
        if int(255*(cp.light-num)/32) > 255:

            color=255
        else:
            color = int(255*(cp.light-num)/32)

        if int(255*(cp.light-num)/32) < 0:
            color=0
       
        cp.pixels[ndx]=(0,color,0)


    if i < ndx:
        cp.pixels[i] = (0,255,0)

    elif i > ndx:
        cp.pixels[i] = (0,0,0)
    
    i = i + 1
        

        