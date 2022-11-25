import folium 
import pandas as pd

read_file = pd.read_csv ('Volcanoes.txt')

Latitude = read_file["LAT"]
Longitde = read_file["LON"]
State = read_file["LOCATION"]

Latitude_list = Latitude.to_list()
Longitude_list = Longitde.to_list()
state_list = State.to_list()

m = folium.Map(location=[Latitude_list[0],Longitude_list[0]])
#fg = folium.FeatureGroup(name="US MAP")    
m.save("index.html")
tooltip = "Click me!"

for i in range(len(Latitude_list)):
    
    state = state_list[i]
    print(Latitude_list[i],Longitude_list[i],state)
    folium.Marker([Latitude_list[i],Longitude_list[i]], popup=state,tooltip=tooltip).add_to(m)
    
#m.add_child(fg)
m.save("index.html")



    
