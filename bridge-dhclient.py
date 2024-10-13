import time

time.sleep(10)

import subprocess
from ping3 import ping
from gpiozero import LED
import os

resetKey = LED(6)
powerKey = LED(5)
pingurl = 'google.com'
DEBUG = True if os.getenv('DEBUG') == 'True'  else False


def log(msg):
    if DEBUG:
        print(msg)

def reset():
    resetKey.on()
    time.sleep(0.5)
    resetKey.off()

def power():
    powerKey.on()
    time.sleep(0.5)
    powerKey.off()


def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully ran: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e}")

def enableDHClient():
    run_command('sudo dhclient usb0')
    time.sleep(2)


def restartDHClient():
    reset()
    time.sleep(30)
    enableDHClient()


def run():
    enableDHClient()
    while True:
        count = 0
        Failed = True
        while Failed:
            time.sleep(1)
            response = ping(pingurl)
            log(f'Response: {response}, count:{count}')
            if response:
                count = 0
                Failed = False
                break
            count+= 1
            if count == 30:
                break

            if (count % 5 == 0):
                enableDHClient()

        if count >= 30:
            restartDHClient()
            count = 0
run()
