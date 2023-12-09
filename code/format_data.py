
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from datetime import datetime

startTime = datetime.now()

# Load GeoJSON data using GeoPandas
gdf = gpd.read_file("data/city-hex-polygons-8.geojson")

# Create a spatial index for faster spatial queries
spatial_index = gdf.sindex

# Function to find the index based on spatial query
def return_index(row):
    
    latitude, longitude = row['latitude'], row['longitude']
    
    # check if latitude and longitude exist:
    if not pd.isnull(latitude) and not pd.isnull(longitude):
        point = Point(longitude, latitude)
        
        # Use spatial index to find potential intersecting polygons
        possible_matches_index = list(spatial_index.intersection(point.bounds))
        
        for idx in possible_matches_index:
            polygon = gdf['geometry'].iloc[idx]
            if point.within(polygon):
                return gdf['index'].iloc[idx]
    
    return 0

# Read the CSV file
df = pd.read_csv("data/sr.csv")
df.rename(columns={"Unnamed: 0": "index"}, inplace=True)



# Create a new column using the spatial query function
df['h3_level8_index'] = df.apply(return_index, axis=1)


# set to number of non-existent latitudes , longitudes or suburbs

error_threshold = (df['latitude'].isna() | df['longitude'].isna() | df['official_suburb'].isna()).sum()
num_of_unjoined= df['h3_level8_index'].value_counts()[0]

df_len = len(df.index)

print(f"Number of unjoined columns: {num_of_unjoined} out of {df_len} - {num_of_unjoined/df_len:.2%}")
if num_of_unjoined < error_threshold:
    df.to_csv('data/sr_my_hex.csv', index=False)
else:
    print(error_threshold, num_of_unjoined)
    print("Error")

elapsed_time = datetime.now() - startTime
print(f"Elapsed time: {elapsed_time.total_seconds():.2f} seconds")