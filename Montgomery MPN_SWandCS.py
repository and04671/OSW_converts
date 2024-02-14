gpkg_path = r'C:\Users\cole5\OneDrive - UW\Work\Data and Geographies\Sidewalks Datasets\MontgomeryMD\MD_Layers.gpkg'
roads = gpkg_path + "|layername=Sel_Road_Surface"
network = gpkg_path + "|layername=Sel_Ped_Network"

Roads = iface.addVectorLayer(roads, "Roads", "ogr")
Network = iface.addVectorLayer(network, "Network", "ogr")

#dissolve road polygon features into one
dissolved_roads = processing.run("native:dissolve", 
{'INPUT':Roads, 'OUTPUT':'memory:'})['OUTPUT']
Step1 = QgsProject.instance().addMapLayer(dissolved_roads)

#extract just the sidewalks and crossings by expression
exp = "(MPN_LINKTYPE = '3') OR (MPN_LINKTYPE = '2' AND MPN_PATHWIDTH != '4')"
extract = processing.run("native:extractbyexpression",
{'INPUT':Network,'EXPRESSION':exp,'OUTPUT':'memory:'})['OUTPUT']
Step2 = QgsProject.instance().addMapLayer(extract)

#select features entirely within road polygon, then invert (gets rid of mid-road 'crossings')
selection = processing.run("native:selectbylocation",
{'INPUT': Step2, 'PREDICATE':[6],'INTERSECT': Step1})
Step2.invertSelection()

#saves inverted selection to new layer (can't figure out how to save inside original gpkg)
#this particular algorithm creates a string, not a vector layer
fnout= r'C:\Users\cole5\OneDrive - UW\Work\Data and Geographies\Sidewalks Datasets\MontgomeryMD\StrippedDown.gpkg'
save_sel = processing.run("native:saveselectedfeatures",
{'INPUT':Step2,'OUTPUT':fnout})['OUTPUT']











