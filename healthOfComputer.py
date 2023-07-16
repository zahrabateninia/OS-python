#!/usr/bin/env python3
# I wrote this code in nano file editor in ubuntu and use chmod to make it executable and executed it by using ./healthOfComputer in the terminal
# and before using psutil module I had to install it using pip3 install psutil in the terminal 
# if we dont install it we are given a notFoundModule error!
import shutil
import psutil

def check_disk_usage(disk):

        du = shutil.disk_usage(disk)

        free = du.free/ du.total * 100

        return free> 20

def check_cpu_usage():

        usage = psutil.cpu_percent(1)

        return usage< 75

if not check_disk_usage('/') or not check_cpu_usage():

        print('Error')

else: 

        print('Everything is OK!')

