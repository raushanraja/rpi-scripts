import subprocess
from gpiozero import LED
import time
# led = LED(5) #Ctl On/off 
led = LED(6) # Ctl Restart
led.on()
time.sleep(0.5)
led.off()
