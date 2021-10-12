import geopandas as gpd
import matplotlib.pyplot as plt

#Importing ESRI shapefile and plotting it via GeoPandas
district = gpd.read_file("Shapefiles/districts.shp")
#print(type(district))
#print(district)
#district.plot(color = 'red',edgecolor = 'black')
district.plot(cmap = 'jet',edgecolor = 'black', column = 'district')
plt.show()