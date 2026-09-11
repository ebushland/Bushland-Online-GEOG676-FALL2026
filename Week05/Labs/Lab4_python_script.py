
# create a gdb and garage feature
import arcpy

arcpy.env.workspace = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week05\Labs\codes_env"
folder_path = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week05\Labs"
gdb_name = "Lab4.gdb"
gdb_path = folder_path + "\\" + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week05\Labs\garages.csv"
garage_layer_name = "Garage_Points"
garages = arcpy.MakeXYEventLayer_management(csv_path, "X", "Y", garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + "\\" + garage_layer_name

# open campus gdb, copy building feature class to lab gdb
campus = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week05\Labs\campus.gdb"
buildings_campus = campus + "\\Structures"
buildings = gdb_path + "\\" + "Buildings"

arcpy.Copy_management(buildings_campus, buildings)

#Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + "\\Garage_Points_reprojected", spatial_ref)

# buffer the garages
garagesBuffered = arcpy.Buffer_analysis(gdb_path + "\\Garage_Points_reprojected", gdb_path + "\\Garage_Buffered","150 Meters")

# Intersect our buffer with the buildings
arcpy.Intersect_analysis([garagesBuffered, buildings], gdb_path + "\\Garage_Building_Intersection", "ALL")

arcpy.TableToTable_conversion(gdb_path + "\\Garage_Building_Intersection.dbf", "C:\\Users\\ebush\\Desktop\\TexasAM\\GEOG-676\\GitHub\\GEOG-676-FALL26\\Week05\\Labs", "nearbyBuildings.csv")