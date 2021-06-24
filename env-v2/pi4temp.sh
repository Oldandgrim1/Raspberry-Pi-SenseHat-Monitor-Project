#!/bin/bash
## Change below to match the raspberry pi that you need to get a temperature from.
ssh pi@localhost "vcgencmd measure_temp | egrep -Eo [0-9][0-9] |tr -d '\n'"
