import RPi.GPIO as io
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
'''a,b= temp_hum()
print(a,b)'''