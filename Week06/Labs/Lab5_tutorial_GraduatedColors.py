import arcpy
# Reference to our .aprx
project = arcpy.mp.ArcGISProject(r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week06\Labs\Lab5\Lab5.aprx")
# Grab the first map in the .aprx
campus = project.listMaps('Map')[0]
# Loop through available layers in the map
for layer in campus.listLayers():
    # Check if layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Check if it has a 'renderer' attribute
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is 'GarageParking'
            if layer.name == "GarageParking":
                # Update the copy's renderer to be 'GraduatedColorsRenderer'
                symbology.updateRenderer('GraduatedColorsRenderer')
                # Tell arcpy which field we want to base our choropleth off of
                symbology.renderer.classificationField = "Shape_Area"
                # Set how many classes we'll have 
                symbology.renderer.breakCount = 5
                # Set the color ramp
                symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("NOT GarageParking")
project.saveACopy(r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week06\Labs\Lab5\Lab5_Update.aprx")
