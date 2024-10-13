import subprocess
import time


def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully ran: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e}")

# Add bridge interface br0
run_command("sudo brctl addbr br0")
time.sleep(2)

# Add eth0 to br0
run_command("sudo brctl addif br0 eth0")

# Add rmnet_mhi0.1 to br0
run_command("sudo brctl addif br0 usb0")

# Startup br0 using ifconfig
run_command("sudo ifconfig br0 up")
