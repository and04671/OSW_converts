mc=iface.mapCanvas()
layer = mc.currentLayer()
dpr = layer.dataProvider()
pfx = 'MPN_'

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

def addFld(layer, fldname, type):
    dpr = layer.dataProvider()
    if type == "string":
        dpr.addAttributes([QgsField(fldname, QVariant.String)])
    if type == "integer":
        dpr.addAttributes([QgsField(fldname, QVariant.Int)])
    layer.updateFields()
#comment




for feature in layer.getFeatures():
    new_name = {feature.fieldNameIndex('highway'): 'footway'}
    dpr.changeAttributeValues({feature.id(): new_name})

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

#addPfx(layer, pfx)
#addFld(layer, "highway","string")
#addFld(layer, "footway","string")
# addFld(layer, "width","integer")
# addFld(layer, "crossing:markings","string")



