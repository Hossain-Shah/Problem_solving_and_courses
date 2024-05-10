import pandas as pd
import geopandas as gpd

from shapely.geometry import LineString

from learntools.core import binder
binder.bind(globals())
from learntools.geospatial.ex2 import *

# Load the data and print the first 5 rows
birds_df = pd.read_csv("../input/geospatial-learn-course-data/purple_martin.csv", parse_dates=['timestamp'])
print("There are {} different birds in the dataset.".format(birds_df["tag-local-identifier"].nunique()))
birds_df.head()

birds = gpd.GeoDataFrame(birds_df, geometry=gpd.points_from_xy(birds_df['location-long'], birds_df['location-lat']))

birds.crs = {'init': 'epsg:4326'}

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
americas = world.loc[world['continent'].isin(['North America', 'South America'])]
americas.head()

birds_gdf = americas.plot(figsize=(8,8), color='whitesmoke', linestyle=':', edgecolor='black')
birds.to_crs(epsg=32630).plot(markersize=1, ax=birds_gdf)

path_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: LineString(x)).reset_index()
path_gdf = gpd.GeoDataFrame(path_df, geometry=path_df.geometry)
path_gdf.crs = {'init' :'epsg:4326'}

# GeoDataFrame showing starting point for each bird
start_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: x[0]).reset_index()
start_gdf = gpd.GeoDataFrame(start_df, geometry=start_df.geometry)
start_gdf.crs = {'init' :'epsg:4326'}

# Show first five rows of GeoDataFrame
start_gdf.head()

end_gdf = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: x[-1]).reset_index()
end_gdf = gpd.GeoDataFrame(end_gdf, geometry=end_gdf.geometry)
end_gdf.crs = {'init' :'epsg:4326'}

start_gdf = americas.plot(figsize=(8,8), color='whitesmoke', linestyle=':', edgecolor='black')
birds.to_crs(epsg=32630).plot(markersize=1, ax=start_gdf)
end_gdf = americas.plot(figsize=(8,8), color='whitesmoke', linestyle=':', edgecolor='black')
birds.to_crs(epsg=32630).plot(markersize=1, ax=end_gdf)
path_gdf = americas.plot(figsize=(8,8), color='whitesmoke', linestyle=':', edgecolor='black')
birds.to_crs(epsg=32630).plot(markersize=1, ax=path_gdf)

protected_filepath = "../input/geospatial-learn-course-data/SAPA_Aug2019-shapefile/SAPA_Aug2019-shapefile/SAPA_Aug2019-shapefile-polygons.shp"

protected_areas = gpd.read_file(protected_filepath)

south_america = americas.loc[americas['continent']=='South America']

ax = protected_areas.plot(figsize=(8,8), color='whitesmoke', linestyle=':', edgecolor='black')
south_america.to_crs(epsg=32630).plot(markersize=1, ax=ax)

P_Area = sum(protected_areas['REP_AREA']-protected_areas['REP_M_AREA'])
print("South America has {} square kilometers of protected areas.".format(P_Area))

south_america.head()

totalArea = sum(south_america.geometry.to_crs(epsg=3035).area) / 10**6

percentage_protected = P_Area/totalArea
print('Approximately {}% of South America is protected.'.format(round(percentage_protected*100, 2)))

bird = protected_areas.plot(figsize=(8,8), color='whitesmoke', linestyle=':', edgecolor='black')
birds.to_crs(epsg=4326).plot(markersize=1, ax=bird)
america = protected_areas.plot(figsize=(8,8), color='whitesmoke', linestyle=':', edgecolor='black')
south_america.to_crs(epsg=4326).plot(markersize=1, ax=america)

