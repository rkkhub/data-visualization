from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from shapely.geometry import Polygon
import geopandas as gp
import csv

world = gp.read_file(gp.datasets.get_path('naturalearth_lowres'))

europe = (world.loc[world['continent'] == 'Europe'])
print(europe.shape)
print(europe.dtypes)
print(europe.columns)
print(europe.head(10))

names = [country for country in europe.name]
print(f"names: {len(names)}")

countries = []
[countries.append(country) if type(item) == Polygon else [countries.append(country) for i in list(item)] for item, country in zip(europe.geometry, names)]
print(f"countries: {len(countries)}")
with open("countries.csv", 'w+', newline ='') as f:
    write = csv.writer(f)
    write.writerows(countries)
    
# polygons = []
# [polygons.append(item) if type(item) == Polygon else [polygons.append(i) for i in list(item)] for item in europe.geometry]

# xs, ys = [], []
# xs = [list(polygon.boundary.coords.xy[0]) for polygon in polygons]
# ys = [list(polygon.boundary.coords.xy[1]) for polygon in polygons]

# source = ColumnDataSource(dict(xs = xs, ys = ys, countries = countries))

# p = figure(title = 'Europe', tools = 'pan, wheel_zoom, box_zoom, reset, hover, save', tooltips = [('Countries', '@countries')],
#            x_range = (-30, 60), y_range = (30, 85), x_axis_location = None, y_axis_location = None)

# p.patches('xs', 'ys', fill_alpha = 0.7, fill_color = 'green', line_color = 'black', line_width = 0.5, source = source)
# show(p)
