#!/bin/bash
sudo mount /dev/sda /media/usb
sudo cat /var/log/boot.log > /media/usb/boot.log
sudo cat /var/log/dmesg > /media/usb/dmesg.log
sudo umount /media/usb
