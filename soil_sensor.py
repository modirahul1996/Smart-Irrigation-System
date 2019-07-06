'''if moisture is detected in soil then soil_moisture
function return zero otherwise 1'''


import RPi.GPIO as io
import time
io.setwarnings(False)
io.setmode(io.BCM)

DO=5#BOARD PIN 29
io.setup(DO,io.IN)
io.setup(6,io.OUT)#BOARD PIN 31
io.output(6,1)

def soil_moisture():
    if io.input(DO)==True:
        q=io.input(DO)
        #for buzzer
        io.output(6,0)
        time.sleep(.2)
        io.output(6,1)
        return(q)
    else:
        t=io.input(DO)
        return(t)
#soil_moisture()
