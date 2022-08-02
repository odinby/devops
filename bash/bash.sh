#!/bin/bash

#ping -c9 google.com

sed -i 's/L/S/g' ./1.txt

PER=$(ls | grep '.sh'| sed 's/\.sh//g')
echo $PER
