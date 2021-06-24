#!/bin/bash

ssh pi@localhost "vcgencmd measure_temp | egrep -Eo [0-9][0-9] |tr -d '\n'"
