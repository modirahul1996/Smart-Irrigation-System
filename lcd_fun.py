import RPi.GPIO as io
import time
#import sys
io.setwarnings(False)
io.setmode(io.BCM)
E=2#3
RS=3#5   
d0=4#7
d1=5#29
d2=6#31
d3=7#26
d4=8#24
d5=9#21
d6=10#19
d7=11#23
io.setup(E,io.OUT)
io.setup(RS,io.OUT)
io.setup(d0,io.OUT)
io.setup(d1,io.OUT)
io.setup(d2,io.OUT)
io.setup(d3,io.OUT)
io.setup(d4,io.OUT)
io.setup(d5,io.OUT)
io.setup(d6,io.OUT)
io.setup(d7,io.OUT)

def send_a_command(command):
    pin=command
    port(pin);
    io.output(RS,0)
    io.output(E,1)
    time.sleep(.01)
    io.output(E,0)
    #pin=0
    #port(pin);

def send_a_character(character):
    pin=character
    port(pin);
    io.output(RS,1)
    io.output(E,1)
    time.sleep(.01)
    io.output(E,0)
    #pin=0
    #port(pin);

def port(pin):
    if(pin&0x01 == 0x01):
        io.output(d0,1)
    else:
        io.output(d0,0)
            
    if(pin&0x02 == 0x02):
        io.output(d1,1)
    else:
        io.output(d1,0)
            
    if(pin&0x04 == 0x04):
        io.output(d2,1)
    else:
        io.output(d2,0)
            
    if(pin&0x08 == 0x08):
        io.output(d3,1)
    else:
        io.output(d3,0)
            
    if(pin&0x10 == 0x10):
        io.output(d4,1)
    else:
        io.output(d4,0)
        
    if(pin&0x20 == 0x20):
        io.output(d5,1)
    else:
        io.output(d5,0)
            
    if(pin&0x40 == 0x40):
        io.output(d6,1)
    else:
        io.output(d6,0)
            
    if(pin&0x80 == 0x80 ):
        io.output(d7,1)
    else:
        io.output(d7,0)

'''while 1:
    send_a_command(0x01)
    send_a_command(0x38)
    send_a_command(0x0E)
    send_a_character(0x48)             
    send_a_character(0x45)                  
    send_a_character(0x59)                    
    send_a_character(0x2C)
    send_a_command(0xC3)
    send_a_character(0x22)
    send_a_character(0x53)                    
    send_a_character(0x55)
    send_a_character(0x4D)
    send_a_character(0x41)
    send_a_character(0x4E)
    send_a_character(0x20)
    send_a_character(0x53)
    send_a_character(0x49)
    send_a_character(0x4E)
    send_a_character(0x47)
    send_a_character(0x48)
    send_a_character(0x22)
    time.sleep(0.3)
    '''

def lcd_show(x):
    l=x
    q=[]
    for i in l:
        p=ord(i)
        b=hex(p)
        q.append(b)
    print(q)
    while 1:
        send_a_command(0x01)
        send_a_command(0x38)
        send_a_command(0x0E)
        c=0
        for i in q:
            c=eval(i)
            send_a_character(c)
            
        time.sleep(1)
    
    
    

