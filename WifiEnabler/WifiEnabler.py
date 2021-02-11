#!/usr/bin/python3
# wifi hotspot enabler

import os
os.system("cls")
print("\n\n\n")
print("Wifi Hotspot Enabler")
print("(C) 2021 Cyber Learner. All right reserved.")
print()
ssid = "MyNet007"
key = "myhotpass"

cmd = "0"
while cmd != 3:
    print("1: Start Hotspot")
    print("2: Stop Hotspot")
    print("3: Exit")
    cmd = input("Please Enter Your Choice (1,2,3): ")
    if cmd == "1":
        print("Starting Hotspot +++++++++")
        os.system("netsh wlan set hostednetwork mode=allow ssid=" + ssid + " key=" + key)
        os.system("netsh wlan start hostednetwork")
    elif cmd == "2":
        print("Stopping Hotspot +++++++++")
        os.system("netsh wlan stop hostednetwork")
    elif cmd == "3":
        print("Exiting +++++++++")
        quit()
    else:
        print("Bad Input 'Please Enter only (1,2,3)'")
        os.system("pause")
