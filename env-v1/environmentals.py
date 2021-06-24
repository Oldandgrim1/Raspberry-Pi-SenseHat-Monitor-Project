#Imports for sensehat, time and sleep.
from sense_hat import SenseHat
from time import sleep
from time import asctime

#Variables, note that you can remove temp, humidity or pressure and use others such as temperature from humidity.
#Recommend that you set the colors below to be different than in the loop.
#The below section can also be largely removed except for declaring sense = SenseHat().
#I'm just playing around here and learning python so please don't kill me.
#Import OS and subprocess is for eventually pushing the log output to csv and/or SQL.

sense = SenseHat()
sense.set_rotation(180) #Set what you need here.
temp = round(sense.get_temperature()*1.8 +32)
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temp is %d F Humid. is %d percent Pres. is %d mbars' %(temp,humidity,pressure)
sense.show_message(message, scroll_speed=(0.033),text_colour=[255,255,255], back_colour= [0,0,0])
sense.clear()

#Loops, add your own home directory or other directory under log = open()

while True:
    log = open("/home/pi/test.txt",'w')
    now = str(asctime())
    log.write(now + " " + message + "\n")
    temp = round(sense.get_temperature()*1.8 +32) #Modify this line to "temp = round(sense.get_temperature())" for Celcius only.
    humidity = round(sense.get_humidity())
    pressure = round(sense.get_pressure())
    print(message)
    sense.show_message(message, scroll_speed=(0.030),text_colour=[64,0,0], back_colour= [0,0,0])
    log.close()
    sleep(5)