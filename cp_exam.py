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
    
    