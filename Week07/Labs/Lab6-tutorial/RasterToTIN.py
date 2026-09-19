import arcpy

tx_dem = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\tx_dem"
gdb = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\Lab6-tutorial.gdb"
z_tolerance = 250.3
max_points = 1500000
z_factor = 1
arcpy.ddd.RasterTin(tx_dem, gdb + "/tx_dem_tin", z_tolerance, max_points, z_factor)