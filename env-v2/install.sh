#!/bin/bash

echo "Installs env-v2 and also the systemd service" 
cp env-v2.csv /home/pi
cp env.py /home/pi
chmod +x /home/pi/env.py
sleep 1
echo "Copy service file to /lib/systemd/system, this may ask for your password"
sleep 1
sudo cp env.service /lib/systemd/system
sudo systemctl enable env
sudo service env start
