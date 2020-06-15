from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
from pathlib import Path
import geopandas as gpd
from shapely.geometry import Polygon
import pandas as pd
import json

file_shapefile = Path("dependency/usa-states-2018/usa-states-2018.shp")
file_save = Path("dependency/usa-states-2018/data.json")

df_states = gpd.read_file(file_shapefile)
names = [state for state in df_states.NAME]
states, polygons = [], []
[states.append(state) if type(item) == Polygon else [states.append(state) for i in list(item)] for item, state in zip(df_states.geometry, names)]
[polygons.append(item) if type(item) == Polygon else [polygons.append(i) for i in list(item)] for item in df_states.geometry]
xs, ys = [], []
xs = [list(polygon.boundary.coords.xy[0]) for polygon in polygons]
ys = [list(polygon.boundary.coords.xy[1]) for polygon in polygons]

data = dict(xs = xs, ys = ys, states = states)
# with open(file_save, 'w') as f:
#     json.dump(data, f)

source = ColumnDataSource(data)
p = figure(title="geo-spacial visualization",
           plot_width=750,
           plot_height=506,
           tools="crosshair")
p.patches(source=source,
          xs='xs',
          ys='ys',
          fill_color="#dddddd",
          fill_alpha=0.9,
          line_color="white",
          line_width=0.5)
p.axis.axis_label = None
p.sizing_mode = "scale_both"
p.axis.visible = False
p.outline_line_color = None
p.grid.grid_line_color = None
p.toolbar_location = None

show(p)
