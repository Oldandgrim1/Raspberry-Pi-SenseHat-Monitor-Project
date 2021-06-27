Version 2 of the Raspberry Pi Sense Hat temperature monitoring project. This version is capable of remotely getting CPU temperatures from other Raspberry Pi computers in your network.

Changelog: 

1. Writing to csv, the output now logs to env-v2.csv by default.
2. There are five included shell scripts that ssh in as the pi user to a remote raspberry pi and run 'vcgencmd measure_temp' and return that as an string which is then converted to integer and displayed on the sense hat.

Install instructions: 

chmod +x install.sh then run ./install.sh from the directory you cloned the project to (should be /home/pi/Raspberry-Pi-SenseHat-Monitor-Project) and run.
Once the service registers it will autostart, if not then check where the script copied the files, if you aren't using the default 'pi' username that can cause the install script to fail. If it does, please reach me on twitter @oldngrim1 or on github.com if you need help.