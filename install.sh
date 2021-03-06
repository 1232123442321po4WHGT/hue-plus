#!/bin/bash

# A simple script to install hue-plus to a universally availible location (in the path)

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

pip3 install pyserial

ln -s $(pwd)/hue.py /usr/bin/hue
ln -s $(pwd)/picker.py /usr/bin/hue-picker
ln -s $(pwd)/hue-ui.py /usr/bin/hue-ui

mkdir /var/lib/hue-plus
cp previous.p /var/lib/hue-plus/previous.p

echo "Install PyQt5 to run the UI"
echo "Now you can run 'hue', 'hue-picker' or 'hue-ui' from anywhere!"
