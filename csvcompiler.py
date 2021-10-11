import json as js
import csv
from itertools import zip_longest
from os import name
data = {}
with open("backup.json",'r') as a:
    data = js.load(a)

lats = []
lons = []
names = []
details = ["Latitude","Longitude","Room"]
for i in data:
    lats.append(data[i]["latitude"])
    lons.append(data[i]["longitude"])
    names.append(data[i]["nodename"].replace("87-2-",'').replace("87-1-",''))

data = [lats,lons,names]
export_data = zip_longest(*data, fillvalue = '')
with open('data.csv','w',newline='') as f:
    write = csv.writer(f)
    write.writerow(("Latitude","Longitude","Room"))
    write.writerows(export_data)

