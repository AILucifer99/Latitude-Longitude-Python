import folium
import matplotlib.pyplot as plt

Latitude = 37.4220656
Longitude = -122.0840897

mapPlot = folium.Map(location = [Latitude, Longitude])
plt.imshow(mapPlot)

print(mapPlot)

