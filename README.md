# ☀️ GES (Power Plant Site Selection) Raster Normalization & AHP Suitability Analysis

This project provides a full workflow for preprocessing raster datasets and performing **site suitability analysis** for Solar Power Plants using **AHP (Analytic Hierarchy Process)**. It includes:

- Raster normalization to AHP scale (1–9),
- Application of AHP weights via Raster Calculator,
- Output: a final suitability map as a GeoTIFF raster.

---

## 📌 Project Overview

This project helps automate and standardize the preprocessing steps required for AHP in a GIS-based solar site selection project.

## 📁 Folder Structure
ges/
├── DNI.tif
├── GHI.tif
├── slope.tif
├── ...
├── normalize_rasters.py
├── output/
│ ├── norm_DNI.tif
│ ├── norm_GHI.tif
│ └── ...

## Step 2: Apply AHP Weights (Raster Calculator)
Once rasters are normalized (1–9), apply AHP weights using QGIS or a custom script.

Example formula in QGIS Raster Calculator:

  ("norm_DNI@1" * 0.30) +
  ("norm_GHI@1" * 0.25) +
  ("norm_slope@1" * 0.15) +
  ("norm_aspect@1" * 0.10) +
  ("norm_temperature@1" * 0.10) +
  ("norm_distance_to_grid@1" * 0.05) +
  ("norm_distance_to_road@1" * 0.05)

## Replace weights with your AHP results. The result will be a suitability map (values between 1–9).

# Input Raster Suggestions
You can use any of the following raster layers:

  Direct Normal Irradiance (DNI)
  Global Horizontal Irradiance (GHI)
  Slope 
  Aspect
  Temperature
  Land Use / Land Cover
  Distance to Roads
  Distance to Electric Grid
  Protected Areas (masked out)

## Output
  norm_*.tif: Normalized input rasters (1–9 scale)
  suitability_map.tif: Final result showing most suitable areas (high = better)
