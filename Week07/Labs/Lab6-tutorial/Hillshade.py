import arcpy

tx_dem = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\tx_dem"
gdb = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\Lab6-tutorial.gdb"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(tx_dem, gdb + "/tx_hillshade", azimuth, altitude, shadows, z_factor)