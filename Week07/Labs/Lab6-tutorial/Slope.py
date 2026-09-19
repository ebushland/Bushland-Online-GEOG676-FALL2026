import arcpy

tx_dem = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\tx_dem"
gdb = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\Lab6-tutorial.gdb"
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
z_unit = "METER"
arcpy.ddd.Slope(tx_dem, gdb + "/tx_dem_slopes", output_measurement, z_factor, method, z_unit)