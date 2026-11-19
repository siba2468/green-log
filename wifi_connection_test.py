
import network
import time

SSID = "SSID"
PASSWORD = "PASSWORD"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Connecting...")

for i in range(20):
    if wifi.isconnected():
        break
    time.sleep(1)

if wifi.isconnected():
    print("Connected!")
    print(wifi.ifconfig())
else:
    print("Connection failed")
    wifi.active(False)
