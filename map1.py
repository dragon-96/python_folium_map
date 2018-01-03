import folium
import pandas
df=pandas.read_excel("log_lat.xlsx")
lat=list(df["Latitude"])
lon=list(df["Longitude"])
nm=list(df["Place Name"])
map=folium.Map(location=[22.7781776,86.2697244],zoom_start=6,tiles="Mapbox Bright")
fgs=folium.FeatureGroup(name="States")
for lt,ln,n in zip(lat,lon,nm):
    fgs.add_child(folium.Marker(location=[lt,ln],popup=n+"-Created By Sumit",
    icon=folium.Icon(color='green')))
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"]<10000000
else "orange" if 10000000<=x["properties"]["POP2005"]<20000000 else "red"}))

map.add_child(fgs)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("map1.html")
