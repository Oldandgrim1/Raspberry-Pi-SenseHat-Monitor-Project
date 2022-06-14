#!/usr/bin/env python3

from sense_hat import SenseHat
from time import asctime, sleep
import subprocess
import sys
import csv
sys.stdout.reconfigure(encoding='utf-8') ##Encodes stdout to utf-8 which removes preceeding 'b' from script output.

##Code starts here.
sys.stdout.write
sense = SenseHat()
sense.set_rotation(180)

while True:
    #For the below subprocess runs I would suggest you create a user that has limited sudo access to only run 'vcgencmd measure_temp'
    #Note that you can add or remove scripts from below then remove the associated variables.
    #You can remove subprocess.run lines and associated code lines depending on how many raspberry pis you own and how many you want to get temperature data from.
    log = open("/home/pi/env-v2.csv",'a+')
    pi1 = subprocess.run(['/home/pi/code/env-v2/pi4temp.sh'],universal_newlines= True, capture_output= True) 
    pi2 = subprocess.run(['/home/pi/code/env-v2/pi1temp.sh'],universal_newlines= True, capture_output= True)
    pi3 = subprocess.run(['/home/pi/code/env-v2/pi2temp.sh'],universal_newlines= True, capture_output= True)
    pi4 = subprocess.run(['/home/pi/code/env-v2/pi3temp.sh'],universal_newlines= True, capture_output= True)
    pi1int = int(pi1.stdout)
    pi2int = int(pi2.stdout)
    pi3int = int(pi3.stdout)
    pi4int = int(pi4.stdout) 
    atemp = round(sense.get_temperature()) #ambient air temp around the local sense hat.
    message = ', AmbT %d C, pi1: %d C, pi2: %d C, pi3: %d C, pi4: %d C' %(atemp,pi1int,pi2int,pi3int,pi4int) #Comma separated in this version.
    sense.show_message (message, scroll_speed=(0.033),text_colour=[128,128,128], back_colour= [0,0,0]) #change foreground and background colors here inside the list brackets.
    now = str(asctime())
    log.write(now + " " + message + "\n")
    log.close
    sleep(5)
     


