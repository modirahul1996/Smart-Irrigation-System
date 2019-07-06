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

'''motor_start()
time.sleep(5)
motor_stop()'''