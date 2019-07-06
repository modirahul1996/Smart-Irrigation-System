#1hum_temp.py
'''import RPi.GPIO as io
import time
import Adafruit_DHT as a
io.setwarnings(False)
io.setmode(io.BCM)
io.setup(2,io.IN)#BOARD PIN 3

def temp_hum():
    while (1):
      hum,temp=a.read_retry(11,2,12)
      #print(temp,hum)
      return(hum,temp)



#2motor_driver.py
import RPi.GPIO as io
import time
io.setwarnings(False)
io.setmode(io.BCM)
io.setup(3,io.OUT)#BOARD PIN 5
io.setup(4,io.OUT)#BOARD PIN 7
io.output(3,1)

def motor_start():
       io.output(3,1)
       io.output(4,0)
       print('motor start\n')
       
def motor_stop():
       io.output(3,0)
       io.output(4,0)
       print('motor stop\n')




#3soil_sensor.py
if moisture is detected in soil then soil_moisture
function return zero otherwise 1


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
#soil_moisture()'''



#4irrigation_system.py

import hum_temp as ht
import motor_driver as md
import soil_sensor as ss
import time
import lcd_fun as lcd




while(1):
    h,t=ht.temp_hum()#h=humidity,t=temperature
    print('temp=',t,'\n','hum=',h)
    q=ss.soil_moisture()
    print('q=',q)
    lcd.send_a_command(0x01)
    lcd.send_a_command(0x38)
    lcd.send_a_command(0x0E)
    lcd.send_a_character(ord('T'))
    lcd.send_a_character(ord('='))
    
    l=t
    su=[]
    for i in l:
        p=ord(i)
        b=hex(p)
        su.append(b)
    print(su)
    send_a_command(0x01)
    send_a_command(0x38)
    send_a_command(0x0E)
    c=0
    for i in su:
        c=eval(i)
        send_a_character(c)    
        time.sleep(1)
    lcd.send_a_command(0x87)
    lcd.send_a_command(0x0E)
    lcd.send_a_character(ord('H'))
    lcd.send_a_character(ord('='))
    l=h
    s=[]
    for i in l:
        p=ord(i)
        b=hex(p)
        s.append(b)
    print(s)
    send_a_command(0x0E)
    c=0
    for i in s:
        c=eval(i)
        send_a_character(c)    
        time.sleep(1)
    
    lcd.send_a_command(0xC0)
    if (q==1 and t<20 and h<180):
        lcd.send_a_command(0x87)
        lcd.send_a_command(0x0E)
        lcd.send_a_character(ord('S'))
        lcd.send_a_character(ord('o'))
        lcd.send_a_character(ord('i'))
        lcd.send_a_character(ord('l'))
        lcd.send_a_character(ord('='))
        l=q
        su1=[]
        for i in l:
            p=ord(i)
            b=hex(p)
            su1.append(b)
        
        send_a_command(0x0E)

        for i in su1:
            c=eval(i)
            send_a_character(c)    
            time.sleep(1)
        
            md.motor_start()
        
    '''if (q!=1 and t>50 and h<150):
        md.motor_start()
        
    if (q==1 and t<15 and h<150):
        md.motor_stop()
    
    if (q!=1 and t<50 and h<150):
        md.motor_stop()'''



       

