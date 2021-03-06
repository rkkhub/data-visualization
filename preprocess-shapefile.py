from pathlib import Path
from shapely.geometry import Polygon
import geopandas as gpd
import json
from polylabel import polylabel

file_source = Path("shapefile/cb_2018_us_state_500k/cb_2018_us_state_500k.shp")
file_formated = Path("shapefile/usa-states-2018/usa-states-2018.shp")
file_json = Path("shapefile/usa-states-2018-espg4326.json")

"""
Source shapefile contain excess data, and requires projection conversion
"""

df_states = gpd.read_file(file_source)
df_states = df_states.cx[-125:-69, 25.5:49.5]                                       # selecting only required shape/location by coordinates
df_states.drop(["STATEFP", "STATENS", "AFFGEOID","GEOID",
                "STUSPS", "LSAD", "ALAND", "AWATER"],
                axis=1, inplace = True)
# print(df_states.crs)
df_states.to_crs(epsg=4326, inplace=True)                                           # convert projection to a desired espg

df_states.to_file(driver = 'ESRI Shapefile',                                        # save processed shapefie
                  filename = file_formated)


"""
Polygons and multipolygons need to be converted to x and y coordinates for plotting. 
"""

names = [state for state in df_states.NAME]
polygons, states = [], []
[polygons.append(item) if type(item) == Polygon 
else [polygons.append(i) for i in list(item)]
for item in df_states.geometry]                                                     # convert multipolygons to polygons

[states.append(state) if type(item) == Polygon
else [states.append(state) for i in list(item)]
for item, state in zip(df_states.geometry, names)]                                  # assign state names for polygons extracted from multipolygons
xs, ys = [], []
xs = [list(polygon.boundary.coords.xy[0]) for polygon in polygons]
ys = [list(polygon.boundary.coords.xy[1]) for polygon in polygons]
# visual_centers = [(polylabel([list(zip(xs[i], ys[i]))])) for i in range(len(xs))]
# center_xs = [coord[0] for coord in visual_centers]
# center_ys = [coord[1] for coord in visual_centers]
# data = dict(xs = xs, ys = ys, states = states, center_xs=center_xs, center_ys=center_ys)
data = dict(xs = xs, ys = ys, states = states)

with open(file_json, 'w') as f:                                                     # save extracted x and y coordinates 
    json.dump(data, f)
