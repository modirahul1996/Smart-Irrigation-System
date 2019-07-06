import RPi.GPIO as io
import time
io.setwarning(0)
io.setmode(io.BCM)
io.setup(13,io.IN)
const=0.02564
cur_pulse=0
last_pulse=0
k=0
pulse=0
rotations=0
while (True):
    cur_pulse=io.input(13)
    if (cur_pulse!=0 and cur_pulse!=last_pulse):
        start=time.time()
        pulse+=1
    last_pulse=cur_pulse
    if(pulse>5):
        rotations+=1
        end=time.time()
        t=end-start
        pulse=o
    print(rotations*t)







# Madam concept
'''while(True):
    pulse=0
    s=0
    cur_pulse=io.input(13)
    last_pulse=0
    rate_cout=0
    start=time.time()
    while(s<=5):
        if (cur_pulse!=0 & cur_pulse=!last_pulse):
            pulse +=1
        last_pulse=cur_pulse
        rate_cout +=1
        s+=1
    end=time.time()
    time=end-start
    waterflow=time*const
    print('water flow =',waterflow)'''
    
    
