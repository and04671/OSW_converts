#This script adds prefixes to original fields and creates new OSW fields, and changes field values based on original fields

# Define the layer for the function
mc=iface.mapCanvas()
layer = mc.currentLayer()
dpr = layer.dataProvider()


# Something's up running this on geopackage files
#This function adds a prefix to all original fields in current layer
def addPfx(layer, pfx):
    layer.startEditing()
    for field in layer.fields():
        oldname = field.name()
        idx = layer.fields().indexFromName(field.name())
        newname = pfx + oldname
        print(newname, idx)
        layer.renameAttribute(idx, newname)
    layer.updateFields()
    layer.commitChanges()

#This function adds a string or integer field to the current layer
def addFld(layer, fldname, type):
    dpr = layer.dataProvider()
    if type == "string":
        dpr.addAttributes([QgsField(fldname, QVariant.String)])
    if type == "integer":
        dpr.addAttributes([QgsField(fldname, QVariant.Int)])
    layer.updateFields()

#This function changes a field's value based on an expression, the field to edit, and new value
def changeVal(exp, fld, newval):
    layer.startEditing()
    layer.beginEditCommand('Edit')
    request = QgsFeatureRequest(QgsExpression(exp))
    for feature in layer.getFeatures(request):
        oldval = dpr.fieldNameIndex(fld)
        layer.changeAttributeValue(feature.id(), oldval, newval)
    layer.endEditCommand()
    layer.commitChanges()
    print("Complete")

#Add MPN_ prefix to original fields
# addPfx(layer, 'MPN_')

#Add OSW map fields
# addFld(layer, "highway","string")
# addFld(layer, "footway","string")
# addFld(layer, "width","integer")
# addFld(layer, "length","integer")
# addFld(layer, "crossing","string")
# addFld(layer, "crossing:markings","string")

#Change values for new OSW fields
#Change OSW highway field values to footway
# changeVal("MPN_LINKTYPE !='8'", 'highway', 'footway')

#Change OSW footway field values to sidewalk or crossing based on link type and width. Remaining features are not sidewalks or crossings
#..and will be deleted in next script section
# changeVal("MPN_LINKTYPE = '2' AND MPN_PATHWIDTH != '4'", 'footway', 'sidewalk')
# changeVal("MPN_LINKTYPE = '3'", 'footway', 'crossing')

#Change OSW crossing:markings field value based on MPN crosswalktype field
# changeVal("MPN_CROSSWALKTYPE = '1'", 'crossing:markings', 'zebra')
# changeVal("MPN_CROSSWALKTYPE = '2'", 'crossing:markings', 'lines')
# changeVal("MPN_CROSSWALKTYPE = '3'", 'crossing:markings', 'no')

#Change OSW crossing field value based on MPN crossingtype field
#NOT SURE ON THESE
# changeVal("MPN_CROSSINGTYPE = 'Signalized'", 'crossing', 'traffic_signals')
# changeVal("MPN_CROSSINGTYPE = 'Stop Controlled'", 'crossing', 'traffic_signals')
# changeVal("MPN_CROSSINGTYPE = 'Uncontrolled'", 'crossing', 'unmarked')

#Change OSW width and length field values based on MPN SHAPE_length and pathwidth fields
#NOT SURE ON THESE
# changeVal("MPN_PATHWIDTH = 'Stop Controlled'", 'crossing', 'traffic_signals')
# changeVal("MPN_SHAPE_length = 'Uncontrolled'", 'crossing', 'unmarked')

#this script modifies the original file, it does not create new file. Make sure to create backup before running. 



