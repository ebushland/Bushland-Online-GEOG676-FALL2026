import arcpy

gdb = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\tx_dem"
input_raster = gdb + "/tx_dem"
output_file = r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\Week7\Lab6-tutorial\texas_dem_ascii.txt"
arcpy.conversion.RasterToASCII(input_raster, output_file)