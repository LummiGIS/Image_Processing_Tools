import gdal
#in_image = r'C:\gTemp\cemsouth.jpg'
in_image = r"C:\gTemp\2021WillowReplaningingArea.pdf"
x = gdal.Info(in_image)
print(x)

print('done without error')