import arcpy

raster_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_2_Programming_For_GIS_3\ProProject_Practical_Two\RASTER_DATA\ASTGTMV003_N19E072_dem.tif"
desc_obj = arcpy.Describe(raster_path)

# The number of bands in the raster dataset
print(desc_obj.bandCount)

#Raster dataset format (Possible value are Grid, ERDAS IMAGINE, TIFF
print(desc_obj.format)

# Printing height and width
print(desc_obj.height)
print(desc_obj.width)

print(desc_obj.basename)