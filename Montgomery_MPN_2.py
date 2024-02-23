
#establish paths to geopackage, roads polygons layer, and ped network layer from last script (Montgomery_MPN_1)
gpkg_path = r'C:\Users\cole5\OneDrive - UW\Work\Data and Geographies\Sidewalks Datasets\MontgomeryMD\MD_Layers.gpkg'
roads = gpkg_path + "|layername=Road_Surface"
network = gpkg_path + "|layername=Ped_Network"

#add layers at path to QGIS GUI
Roads = iface.addVectorLayer(roads, "Roads", "ogr")
Network = iface.addVectorLayer(network, "Network", "ogr")

#Dissolve road polygon features into one (allows "entirely within" call later)
dissolved_roads = processing.run("native:dissolve", 
{'INPUT':Roads, 'OUTPUT':'memory:'})['OUTPUT']
Step1 = QgsProject.instance().addMapLayer(dissolved_roads)

#Extract just the sidewalks and crossings by expression (gets rid of road 'sidewalks' with no width)
exp = "(MPN_LINKTYPE = '3') OR (MPN_LINKTYPE = '2' AND MPN_PATHWIDTH != '4')"
extract = processing.run("native:extractbyexpression",
{'INPUT':Network,'EXPRESSION':exp,'OUTPUT':'memory:'})['OUTPUT']
Step2 = QgsProject.instance().addMapLayer(extract)

#Select network features "entirely within" dissolved road polygon, then invert (gets rid of mid-road 'crossings')
selection = processing.run("native:selectbylocation",
{'INPUT': Step2, 'PREDICATE':[6],'INTERSECT': Step1})
Step2.invertSelection()

#Save inverted selection to new layer and geopackage called "Stripped Down"
#this particular (native:saveselectedfeatures) algorithm creates a string, not a vector layer
fnout= r'C:\Users\cole5\OneDrive - UW\Work\Data and Geographies\Sidewalks Datasets\MontgomeryMD\StrippedDown.gpkg'
save_sel = processing.run("native:saveselectedfeatures",
{'INPUT':Step2,'OUTPUT':fnout})['OUTPUT']

#could run Stripped Down back through first script











