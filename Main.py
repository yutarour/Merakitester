#This is the program used to map the lcation of the wifi router.

import requests
import os 
import time
import json as js

devicelist = {}
with open("backup.json",'r') as file:
    devicelist = js.load(file)

def enable():
    os.system('netsh wlan connect name="LWSD-WLAN" interface="wi-fi"')
    time.sleep(2)

def disable():
    os.system("netsh wlan disconnect")
    time.sleep(2)

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
    }
url = "http://my.meraki.com/index.json"

ses = requests.Session()
b = 0
while True:
    b+=1
    try:
        #enable()
        resp = ses.get(url=url).json()
    
        lat = resp["config"]["lat"]
        lon = resp["config"]["lng"]
        nodename = resp["config"]["node_name"]
        max_bitrate = resp["client"]["max_device_bitrate"]
        channels = []
        for i in resp["radio_stats"]:
            channels.append(i["channel"])

        if devicelist.get(resp["config"]["mac"])== None:
            devicelist[resp["config"]["mac"]]={
                "latitude":lat,
                "longitude":lon,
                "nodename":nodename,
                "channels":channels,
                "max_bitrate":max_bitrate
            }
            print(nodename)
        if b %10==0:
            with open("backup.json",'w') as file:
                js.dump(devicelist,file,indent=2)
                print(devicelist)
                file.close()
                
    except requests.exceptions.ConnectionError:
        enable()
        time.sleep(2)
        continue
    
    except KeyboardInterrupt:
        with open("backup.json",'w') as file:
            js.dump(devicelist,file,indent=2)
            print(devicelist)
            file.close()
            
    
    

    
    disable()
    #time.sleep(1)
    enable()
    time.sleep(1)


