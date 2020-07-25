from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
from pathlib import Path
import geopandas as gpd
import pandas as pd
import json


file_data = Path("shapefile/usa-states-2018.json")

with open(file_data,"r") as f:
  data = json.load(f)

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
