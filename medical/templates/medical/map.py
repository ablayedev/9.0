import folium


#create map object
m=folium.Map(location=[14.6937000,-17.4440600],zoom_start=12)

#global tooltip
tooltip="Cliquez pour plus de détail"

folium.Marker([14.6937000,-17.4440600],popup='<h2>Optalmologue <br/> Téléphone:78-378-66-12</h2>',tooltip=tooltip).add_to(m)
folium.Marker([14.6937000,-17.4740600],popup='<h2>Optalmologue <br/> Téléphone:78-478-26-12</h2>',tooltip=tooltip).add_to(m)



#generate map
m.save('ophtalmologue.html')