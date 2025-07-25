{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3cf32166-9d2d-40eb-a26d-b602f2b1dd1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DNI.tif normalized\n"
     ]
    }
   ],
   "source": [
    "import rasterio\n",
    "import numpy as np\n",
    "import os\n",
    "\n",
    "def normalize_raster_to_ahp_scale(input_path, output_path, n_classes=9):\n",
    "    with rasterio.open(input_path) as src:\n",
    "        data = src.read(1)\n",
    "        profile = src.profile\n",
    "\n",
    "        nodata_val = src.nodata if src.nodata is not None else 0\n",
    "        mask = data == nodata_val\n",
    "        data_masked = np.ma.masked_array(data, mask=mask)\n",
    "\n",
    "        min_val = data_masked.min()\n",
    "        max_val = data_masked.max()\n",
    "        step = (max_val - min_val) / n_classes\n",
    "\n",
    "        reclassified = np.zeros_like(data_masked, dtype=np.uint8)\n",
    "\n",
    "        for i in range(n_classes):\n",
    "            lower = min_val + i * step\n",
    "            upper = min_val + (i + 1) * step\n",
    "            reclassified[(data_masked >= lower) & (data_masked < upper)] = i + 1\n",
    "\n",
    "        reclassified = np.where(mask, nodata_val, reclassified)\n",
    "\n",
    "        profile.update(dtype=rasterio.uint8, nodata=nodata_val)\n",
    "\n",
    "        with rasterio.open(output_path, 'w', **profile) as dst:\n",
    "            dst.write(reclassified, 1)\n",
    "\n",
    "# Klasörler\n",
    "input_folder = \"/Users/mac/Documents/ges\"\n",
    "output_folder = \"/Users/mac/Documents/ges/output\"\n",
    "\n",
    "# Klasör yoksa oluştur\n",
    "if not os.path.exists(output_folder):\n",
    "    os.makedirs(output_folder)\n",
    "\n",
    "# Raster listesi\n",
    "raster_list = [\n",
    "    \"DNI.tif\"\n",
    "]\n",
    "\n",
    "for raster in raster_list:\n",
    "    input_path = os.path.join(input_folder, raster)\n",
    "    output_path = os.path.join(output_folder, \"norm_\" + raster)\n",
    "    normalize_raster_to_ahp_scale(input_path, output_path)\n",
    "    print(f\"{raster} normalized\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
