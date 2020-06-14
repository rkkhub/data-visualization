from pathlib import Path
import geopandas as gpd

file_shapefile = Path("source_file.shp")
df_states = gpd.read_file(file_shapefile)
df_states = df_states.cx[-125:-69,25.5:49.5]                                    # selecting only required shapes/locations
df_states.drop(["column1","column2","column3"], axis=1, inplace = True)         # drop columns that are not required
df_states.to_crs(epsg=2163, inplace=True)                                       # convert projection to a desired espg
df_states.to_file(driver = 'ESRI Shapefile', filename= Path("targed_file.shp")) # save the processed shapefie



