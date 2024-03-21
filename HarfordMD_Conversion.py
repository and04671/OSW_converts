#start from breaking dataset down into groups 1-100x
#either gridded or randomly assigned

gpkg_path = r'C:\Users\cole5\OneDrive - UW\Work\Data and Geographies\Sidewalks Datasets\HarfordCT\HarfordOriginal.gpkg'
sdwk = gpkg_path + "|layername=Original_w_GROUP"
layer = iface.addVectorLayer(sdwk, "Sidewalks", "ogr")

#now I need to loop this whole thing over each group value
for each in range(1,101):
#select features with particular group value 1-100
    extract = processing.run("qgis:extractbyattribute", 
    {'INPUT':layer,
    'FIELD':'GROUP',
    'OPERATOR':0,
    'VALUE':each,
    'OUTPUT':'memory:'})['OUTPUT']
    
#create centerlines from extracted features
#chordal axis function from geosimplification plugin
#limit of 1000 features per run (x 75 times)
#this may be problem: process erases all attributes and turns into one polyline
    processing.runAndLoadResults("geo_sim_processing:chordalaxis", 
    {'INPUT':extract,
    'CORRECTION':False,
    'OUTPUT':'TEMPORARY_OUTPUT',
    'TRIANGLES':'TEMPORARY_OUTPUT'})    