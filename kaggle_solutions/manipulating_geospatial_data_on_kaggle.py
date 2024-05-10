import math
import pandas as pd
import geopandas as gpd
#from geopy.geocoders import Nominatim            
from learntools.geospatial.tools import Nominatim 

import folium 
from folium import Marker
from folium.plugins import MarkerCluster

from learntools.core import binder
binder.bind(globals())
from learntools.geospatial.ex4 import *


def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')

# Load and preview Starbucks locations in California
starbucks = pd.read_csv("../input/geospatial-learn-course-data/starbucks_locations.csv")
starbucks.head()

print(starbucks.isnull().sum())

# View rows with missing locations
rows_with_missing = starbucks[starbucks["City"]=="Berkeley"]
rows_with_missing

geolocator = Nominatim(user_agent="kaggle_learn")


def my_geocoder(row):
    point = geolocator.geocode(row).point
    return pd.Series({'Latitude': point.latitude, 'Longitude': point.longitude})

berkeley_locations = rows_with_missing.apply(lambda x: my_geocoder(x['Address']), axis=1)
starbucks.update(berkeley_locations)

m_2 = folium.Map(location=[37.88,-122.26], zoom_start=13)

# Add points to the map
for idx, row in berkeley_locations.iterrows():
    Marker([row['Latitude'], row['Longitude']]).add_to(m_2)

# Show the map
embed_map(m_2, 'q_2.html')

CA_counties = gpd.read_file("../input/geospatial-learn-course-data/CA_county_boundaries/CA_county_boundaries/CA_county_boundaries.shp")
CA_counties.head()

CA_pop = pd.read_csv("../input/geospatial-learn-course-data/CA_county_population.csv", index_col="GEOID")
CA_high_earners = pd.read_csv("../input/geospatial-learn-course-data/CA_county_high_earners.csv", index_col="GEOID")
CA_median_age = pd.read_csv("../input/geospatial-learn-course-data/CA_county_median_age.csv", index_col="GEOID")

cols_to_add = CA_pop.join([CA_high_earners, CA_median_age]).reset_index()
CA_stats = CA_counties.merge(cols_to_add, on="GEOID")
CA_stats.crs = {'init': 'epsg:4326'}

CA_stats["density"] = CA_stats["population"] / CA_stats["area_sqkm"]

sel_counties = CA_stats[((CA_stats.high_earners > 100000) &
                         (CA_stats.median_age < 38.5) &
                         (CA_stats.density > 285) &
                         ((CA_stats.median_age < 35.5) |
                         (CA_stats.density > 1400) |
                         (CA_stats.high_earners > 500000))
                         
starbucks_gdf = gpd.GeoDataFrame(starbucks, geometry=gpd.points_from_xy(starbucks.Longitude, starbucks.Latitude))
starbucks_gdf.crs = {'init': 'epsg:4326'}

num_stores = len(gpd.sjoin(starbucks_gdf, sel_counties))


m_6 = folium.Map(location=[37,-120], zoom_start=6)

for idx, row in berkeley_locations.iterrows():
    Marker([row['Latitude'], row['Longitude']]).add_to(m_6)

embed_map(m_6, 'q_6.html')


