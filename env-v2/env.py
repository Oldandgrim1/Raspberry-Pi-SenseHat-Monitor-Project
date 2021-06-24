from sense_hat import SenseHat
from time import sleep
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8') ##Encodes stdout to utf-8 which removes preceeding 'b' from script output.

##Code starts here.
sys.stdout.write
sense = SenseHat()
sense.set_rotation(180)
atemp = round(sense.get_temperature())
#For the below subproccess runs I would suggest you create a user that has limited sudo access to only run 'vcgencmd measure_temp'
#note that you can add or remove scripts from below then remove the associated variables.
pi1 = subprocess.run(['/home/pi/env-v2/learningpython/pi4temp.sh'],universal_newlines= True, capture_output= True)
pi2 = subprocess.run(['/home/pi/env-v2/learningpython/pi1temp.sh'],universal_newlines= True, capture_output= True)
pi3 = subprocess.run(['/home/pi/env-v2/learningpython/pi2temp.sh'],universal_newlines= True, capture_output= True)
pi4 = subprocess.run(['/home/pi/env-v2/learningpython/pi3temp.sh'],universal_newlines= True, capture_output= True)
pi1int = int(pi1.stdout)
pi2int = int(pi2.stdout)
pi3int = int(pi3.stdout)
pi4int = int(pi4.stdout)
message = 'AmbT %d, ans1 %d r1 %d r2 %d r3 %d' %(atemp,pi1int,pi2int,pi3int,pi4int)
sense.show_message (message, scroll_speed=(0.033),text_colour=[255,0,0], back_colour= [0,0,0])
sleep(2) 

while True:
    atemp = round(sense.get_temperature())
    #For the below subproccess runs I would suggest you create a user that has limited sudo access to only run 'vcgencmd measure_temp'
    #note that you can add or remove scripts from below then remove the associated variables.
    pi1 = subprocess.run(['/home/pi/env-v2/learningpython/pi4temp.sh'],universal_newlines= True, capture_output= True)
    pi2 = subprocess.run(['/home/pi/env-v2/learningpython/pi1temp.sh'],universal_newlines= True, capture_output= True)
    pi3 = subprocess.run(['/home/pi/env-v2/learningpython/pi2temp.sh'],universal_newlines= True, capture_output= True)
    pi4 = subprocess.run(['/home/pi/env-v2/learningpython/pi3temp.sh'],universal_newlines= True, capture_output= True)
    pi1int = int(pi1.stdout)
    pi2int = int(pi2.stdout)
    pi3int = int(pi3.stdout)
    pi4int = int(pi4.stdout)
    message = 'AmbT %d, ans1 %d r1 %d r2 %d r3 %d' %(atemp,pi1int,pi2int,pi3int,pi4int)
    sense.show_message (message, scroll_speed=(0.033),text_colour=[60,70,0], back_colour= [0,0,0])
    print(message)
     


