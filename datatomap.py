import json as js
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely import geometry
from shapely.geometry import Point,Polygon
import matplotlib.pyplot as plt

street_map = gpd.read_file("map-polygon.shp")
fig,ax = plt.subplots(figsize=(15,15))


df = pd.read_csv('data.csv')
crs = {"init":'epsg:4326'}
df.head()
geomet = [Point(xy) for xy in zip(df["Longitude"],df["Latitude"])]
geodf = gpd.GeoDataFrame(df,crs=crs,geometry=geomet)
geodf.head()

#for x, y, label in zip(street_map.geometry.x, street_map.geometry.y, df["Rooms"]):
#    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")

street_map.plot(ax=ax,alpha=0.4,color='orange')
geodf.plot(ax=ax,markersize=20,color='blue')

for x,y,label in zip(df["Longitude"],df["Latitude"],df["Room"]):
    ax.annotate(label, xy=(x, y), xytext=(0,10), textcoords="offset points")
    
plt.show()