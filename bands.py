import rasterio

with rasterio.open("HS_img/ENMAP01-____L2A-DT0000080509_20240702T070803Z_003_V010501_20241022T170029Z_masked.tif") as src:
    print(src.count)  # number of bands
    print(src.tags()) # global metadata
    for i in range(1, src.count+1):
        print(src.tags(i))  # band-specific metadata
