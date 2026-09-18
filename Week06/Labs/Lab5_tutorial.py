import arcpy
# Reference to our .aprx
project = arcpy.mp.ArcGISProject(r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week06\Labs\Lab5\Lab5.aprx")
#Grab the first map in the .aprx
campus = project.listMaps('Map')[0]
# Loop through available layers in the map
for layer in campus.listLayers():
    # Check that the layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Makes sure symbology has an attribute "renderer"
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is "Structures"
            if layer.name == "Structures":
                # Update the copy's renderer to be "UniqueValueRenderer"
                symbology.updateRenderer('UniqueValueRenderer')
                # Tells arcpy that we want to use "Type" as our unique value
                symbology.renderer.fields = ["Type"]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("NOT Structures")
project.saveACopy(r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week06\Labs\Lab5\Lab5_Update.aprx")
