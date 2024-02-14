mc=iface.mapCanvas()
layer = mc.currentLayer()
dpr = layer.dataProvider()



#somethings up running this on geopackage
def addPfx(layer, pfx):
#a function to add a prefix to all original fields
    layer.startEditing()
    for field in layer.fields():
        oldname = field.name()
        idx = layer.fields().indexFromName(field.name())
        newname = pfx + oldname
        print(newname, idx)
        layer.renameAttribute(idx, newname)
    layer.updateFields()
    layer.commitChanges()

def addFld(layer, fldname, type):
#a function to add a string or integer field to the selected layer
    dpr = layer.dataProvider()
    if type == "string":
        dpr.addAttributes([QgsField(fldname, QVariant.String)])
    if type == "integer":
        dpr.addAttributes([QgsField(fldname, QVariant.Int)])
    layer.updateFields()

#enter feature selection expression, the field to edit, and new value
def changeVal(layer, exp, fld, newval):
    layer.startEditing()
    layer.beginEditCommand('Edit')
    request = QgsFeatureRequest(QgsExpression(exp))
    for feature in layer.getFeatures(request):
        oldval = dpr.fieldNameIndex(fld)
        layer.changeAttributeValue(feature.id(), oldval, newval)
    layer.endEditCommand()
    layer.commitChanges()
    print("Complete")
    
#select features in ped network meeting expression criteria: Pathwidth != 4 and Linktype = 2 or 3
#dissolve road gons
#select subset not meeting 'entirely within' roadpolygons


# addPfx(layer, 'MPN_')

# addFld(layer, "highway","string")
# addFld(layer, "footway","string")
# addFld(layer, "width","integer")
# addFld(layer, "crossing:markings","string")

changeVal(layer, "MPN_LINKTYPE !='8'", 'highway', 'footway2')
# changeVal("MPN_LINKTYPE = '2' AND MPN_PATHWIDTH = '4'", 'footway', 'No sidewalk')



