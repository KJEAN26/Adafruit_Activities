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
number = 0
led=0
while True:
    led=number-1 if cp.switch==False else number + 1
    number = 9 if led < 0 else led
    number = 0 if led >=10 else number
    cp.pixels[number]=  (255,255,255)
    sleep(.5)
    cp.pixels[number]=(0,0,0)
    sleep(.5)

    
    
    
              
   
    

