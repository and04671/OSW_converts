mc=iface.mapCanvas()
layer = mc.currentLayer()
dpr = layer.dataProvider()

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

#Wisam: this is the section of code that dor some reaosn loop through 200 features, then prints complete, instead of all of the features (2000 in the test set)
for feature in layer.getFeatures():
    new_name = {feature.fieldNameIndex('highway'): 'footway'}
    dpr.changeAttributeValues({feature.id(): new_name})
    print(feature.id())
print("Complete")


# with edit(layer):
#     for f in layer.getFeatures():
#         f['footway'] = f['highway']
#         layer.updateFeature(f)    

# layer.startEditing()
# for feature in layer.getFeatures():
#     value = expression.evaluate(feature)
#     layer.changeAttributeValue(feature.id(), index, value)

# features = layer.getFeatures()
# for feature in features:
#     value = expression.evaluate(feature)
#     print(value)
#     feature[new_field_index] = value
#     layer.updateFeature(feature)



#addPfx(layer, 'MPN_')
# addFld(layer, "highway","string")
# addFld(layer, "footway","string")
# addFld(layer, "width","integer")
# addFld(layer, "crossing:markings","string")



