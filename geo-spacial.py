from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
from pathlib import Path
import geopandas as gpd
from shapely.geometry import Polygon
import pandas as pd


file_shapefile = Path("dependency/usa-states-2018/usa-states-2018.shp")
# file_shapefile = Path("dependency/quick-demo/quick-demo.shp")

df_states = gpd.read_file(file_shapefile)
print(f"CRS: {df_states.crs}")
print(df_states.shape)
print(df_states.dtypes)
print(df_states.columns)
print(df_states.head(5))
# print(print(df_states["geometry"].iloc[3]))

# states = []
# [states.append(country) if type(item) == Polygon else [states.append(country) for i in list(item)] for item, country in zip(europe.geometry, names)]

# polygons = []
# [polygons.append(item) if type(item) == Polygon else [polygons.append(i) for i in list(item)] for item in df_states.geometry]

# xs, ys = [], []
# xs = [list(polygon.boundary.coords.xy[0]) for polygon in polygons]
# ys = [list(polygon.boundary.coords.xy[1]) for polygon in polygons]

polygons = []
[polygons.append(item) if type(item) == Polygon else [polygons.append(i) for i in list(item)] for item in df_states.geometry]

xs, ys = [], []
xs = [list(polygon.boundary.coords.xy[0]) for polygon in polygons]
ys = [list(polygon.boundary.coords.xy[1]) for polygon in polygons]

# def getPolyCoords(row, geom, coord_type):
#     """Returns the coordinates ('x|y') of edges/vertices of a Polygon/others"""
#     # Parse the geometries and grab the coordinate
#     geometry = row[geom]
#     # print(geometry.type)
#     if geometry.type == 'Polygon':
#         if coord_type == 'x':
#             # Get the x coordinates of the exterior
#             # Interior is more complex: xxx.interiors[0].coords.xy[0]
#             return list(geometry.exterior.coords.xy[0])
#         elif coord_type == 'y':
#             # Get the y coordinates of the exterior
#             return list(geometry.exterior.coords.xy[1])
#     if geometry.type in ['Point', 'LineString']:
#         if coord_type == 'x':
#             return list(geometry.xy[0])
#         elif coord_type == 'y':
#             return list(geometry.xy[1])
#     if geometry.type == 'MultiLineString':
#         all_xy = []
#         for ea in geometry:
#             if coord_type == 'x':
#                 all_xy.append(list(ea.xy[0]))
#             elif coord_type == 'y':
#                 all_xy.append(list(ea.xy[1]))
#         return all_xy
#     if geometry.type == 'MultiPolygon':
#         all_xy = []
#         for ea in geometry:
#             if coord_type == 'x':
#                 all_xy.append(list(ea.exterior.coords.xy[0]))
#             elif coord_type == 'y':
#                 all_xy.append(list(ea.exterior.coords.xy[1]))
#         return [item for sublist in all_xy for item in sublist]
#     else:
#         # Finally, return empty list for unknown geometries
#         return []

# df_states['x'] = df_states.apply(getPolyCoords, geom='geometry', coord_type='x', axis=1)
# df_states['y'] = df_states.apply(getPolyCoords, geom='geometry', coord_type='y', axis=1)
df_states['x'] = pd.Series(xs)
df_states['y'] = pd.Series(ys)
df_data = df_states.drop('geometry', axis=1).copy()


chart_data = ColumnDataSource(df_data)
p = figure(title="geo-spacial visualization",
           plot_width=640,
           plot_height=400,
           tools="crosshair")

p.patches(source=chart_data,
          xs='x',
          ys='y',
          fill_color="#dddddd",
          fill_alpha=0.9,
          line_color="white",
          line_width=0.5)
p.axis.axis_label = None
# p.sizing_mode = "scale_both"
p.axis.visible = False
p.outline_line_color = None
p.grid.grid_line_color = None
p.toolbar_location = None
show(p)
