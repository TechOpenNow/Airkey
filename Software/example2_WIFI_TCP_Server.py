import airkey
import time

# Initialize the Serial Port with Comm Port
# ttyAMA0/ttyUSB0 for GPIO communication with Raspberry Pi
# COMx for PC 

device = airkey.module(port='COM14', baudrate=115200)    
device.open()

# Check the link with using by sending AT command
device.link_check()
time.sleep(2)

# Connect to the WiFi network and make sure the computer
# is also connected to same network for TCP Server
device.set_WIFI_STA("MYWIFI", 12345678)
time.sleep(2)

# Open NetAssit in the computer and check the IP and Port (can be edited in netassist) of TCP Server
device.set_TCP("172.20.144.128", 8080)
time.sleep(2)

# Set the module configuration mode 6 - UART-TCP passthrough
device.set_working_mode(6)
time.sleep(2)

device.send_data("AAAAAAA")


