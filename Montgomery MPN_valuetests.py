import time

mc=iface.mapCanvas()
layer = mc.currentLayer()
dpr = layer.dataProvider()

def changeVal(exp, fld, newval):
    t0 = time.time()
    
    layer.startEditing()
    layer.beginEditCommand('Edit')
    
    request = QgsFeatureRequest(QgsExpression(exp))
    for feature in layer.getFeatures(request):
        oldval = dpr.fieldNameIndex(fld)
        layer.changeAttributeValue(feature.id(), oldval, newval)
        
    layer.endEditCommand()
    layer.commitChanges()
    
    t1 = time.time()
    total = t1-t0
    print(total)
    
changeVal("MPN_LINKTYPE = *", 'highway', 'footway')

#20k features = 198s (that can't be right...)
#4k features = 4 s



