import rasterio
import numpy as np
import os

def normalize_raster_to_ahp_scale(input_path, output_path, n_classes=9):
    with rasterio.open(input_path) as src:
        data = src.read(1)
        profile = src.profile

        nodata_val = src.nodata if src.nodata is not None else 0
        mask = data == nodata_val
        data_masked = np.ma.masked_array(data, mask=mask)

        min_val = data_masked.min()
        max_val = data_masked.max()
        step = (max_val - min_val) / n_classes

        reclassified = np.zeros_like(data_masked, dtype=np.uint8)

        for i in range(n_classes):
            lower = min_val + i * step
            upper = min_val + (i + 1) * step
            reclassified[(data_masked >= lower) & (data_masked < upper)] = i + 1

        reclassified = np.where(mask, nodata_val, reclassified)
        profile.update(dtype=rasterio.uint8, nodata=nodata_val)

        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(reclassified, 1)

# Folder Paths
input_folder = "/Users/mac/Documents/ges"
output_folder = "/Users/mac/Documents/ges/output"

# Output file
os.makedirs(output_folder, exist_ok=True)

# Rasters
raster_list = [
    "DNI.tif"
    # You can also add other rasters here: "GHI.tif", "Slope.tif", ...
]

# Apply function to each raster
for raster in raster_list:
    input_path = os.path.join(input_folder, raster)
    output_path = os.path.join(output_folder, f"norm_{raster}")
    normalize_raster_to_ahp_scale(input_path, output_path)
    print(f"{raster} normalized")
