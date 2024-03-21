#start with the stripped down output from MPN 2

gpkg = r'C:\Users\cole5\OneDrive - UW\Work\Data and Geographies\Sidewalks Datasets\MontgomeryMD\StrippedDown.gpkg'
base = gpkg + "|layername=StrippedDown"

StrippedDown = iface.addVectorLayer(base, "Base", "ogr")
StrippedDown.setSubsetString("MPN_LINKTYPE = 3")

x = processing.run("gdal:pointsalonglines", {'INPUT':StrippedDown,'GEOMETRY':'geometry','DISTANCE':0.05,'OUTPUT':'TEMPORARY_OUTPUT'})
y = processing.run("gdal:pointsalonglines", {'INPUT':StrippedDown,'GEOMETRY':'geometry','DISTANCE':0.95,'OUTPUT':'TEMPORARY_OUTPUT'})
p = processing.run("native:mergevectorlayers", {'LAYERS':[x['OUTPUT'],y['OUTPUT']],'CRS':QgsCoordinateReferenceSystem('EPSG:4326'),'OUTPUT':r'C:\Users\cole5\OneDrive - UW\Work\Data and Geographies\Sidewalks Datasets\MontgomeryMD\pointsall.geojson'})

CurbPoints = iface.addVectorLayer(p['OUTPUT'], "Points", "ogr")