import math
import geopandas as gpd
import pandas as pd
from shapely.geometry import MultiPolygon

import folium
from folium import Choropleth, Marker
from folium.plugins import HeatMap, MarkerCluster

from learntools.core import binder
binder.bind(globals())
from learntools.geospatial.ex5 import *


def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')

collisions = gpd.read_file("../input/geospatial-learn-course-data/NYPD_Motor_Vehicle_Collisions/NYPD_Motor_Vehicle_Collisions/NYPD_Motor_Vehicle_Collisions.shp")
collisions.head()

m_1 = folium.Map(location=[40.7, -74], zoom_start=11) 
HeatMap(data=collisions[['LATITUDE', 'LONGITUDE']], radius=15).add_to(m_1)

# Show the map
embed_map(m_1, "q_1.html")
m_1

hospitals = gpd.read_file("../input/geospatial-learn-course-data/nyu_2451_34494/nyu_2451_34494/nyu_2451_34494.shp")
hospitals.head()

m_2 = folium.Map(location=[40.7, -74], zoom_start=11) 

HeatMap(data=hospitals[['latitude', 'longitude']], radius=15).add_to(m_2)

# Show the map
embed_map(m_2, "q_2.html")

coverage = gpd.GeoDataFrame(geometry=hospitals.geometry).buffer(10000)
my_union = coverage.geometry.unary_union
outside_range = collisions.loc[~collisions["geometry"].apply(lambda x: my_union.contains(x))]

percentage = round(100*len(outside_range)/len(collisions), 2)
print("Percentage of collisions more than 10 km away from the closest hospital: {}%".format(percentage))


def best_hospital(collision_location):
    name = hospitals.iloc[hospitals.geometry.distance(collision_location).idxmin()]["name"]
    return name

print(best_hospital(outside_range.geometry.iloc[0]))

highest_demand = outside_range.geometry.apply(best_hospital).value_counts().idxmax()

m_6 = folium.Map(location=[40.7, -74], zoom_start=11) 

coverage = gpd.GeoDataFrame(geometry=hospitals.geometry).buffer(10000)
folium.GeoJson(coverage.geometry.to_crs(epsg=4326)).add_to(m_6)
HeatMap(data=outside_range[['LATITUDE', 'LONGITUDE']], radius=9).add_to(m_6)
folium.LatLngPopup().add_to(m_6)

embed_map(m_6, 'm_6.html')

lat_1 = 40.6714
long_1 = -73.8492

lat_2 = 40.6702
long_2 = -73.7612


new_df = pd.DataFrame(
    {'Latitude': [lat_1, lat_2],
        'Longitude': [long_1, long_2]})
new_gdf = gpd.GeoDataFrame(new_df, geometry=gpd.points_from_xy(new_df.Longitude, new_df.Latitude))
new_gdf.crs = {'init' :'epsg:4326'}
new_gdf = new_gdf.to_crs(epsg=2263)

# get new percentage
new_coverage = gpd.GeoDataFrame(geometry=new_gdf.geometry).buffer(10000)
new_my_union = new_coverage.geometry.unary_union
new_outside_range = outside_range.loc[~outside_range["geometry"].apply(lambda x: new_my_union.contains(x))]
new_percentage = round(100*len(new_outside_range)/len(collisions), 2)
print("(NEW) Percentage of collisions more than 10 km away from the closest hospital: {}%".format(new_percentage))

# make the map
m = folium.Map(location=[40.7, -74], zoom_start=11) 
folium.GeoJson(coverage.geometry.to_crs(epsg=4326)).add_to(m)
folium.GeoJson(new_coverage.geometry.to_crs(epsg=4326)).add_to(m)


for idx, row in new_gdf.iterrows():
    Marker([row['Latitude'], row['Longitude']]).add_to(m)
HeatMap(data=new_outside_range[['LATITUDE', 'LONGITUDE']], radius=9).add_to(m)
folium.LatLngPopup().add_to(m)
display(embed_map(m, 'q_6.html'))
