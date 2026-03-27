# **On-the-fly collection of POLARIN data using OPeNDAP**
>NOTE: this notebook has been created by ETT ([source](https://github.com/POLAR-RESEARCH-INFRASTRUCTURE-NETWORK/jupyter-notebooks/blob/bcc03ffc3e7ee23c3728e15725c91fb9a1df456f/data_cookbook/chapters/chapter1/polarin_erddap_querying_tabledap.ipynb)) and has been adjusted to suit the needs of the Transnational Access (TA) webinar scheduled for 9<sup>th</sup> of April 2026 10:00 - 10:45 CEST.

# Welcome to the POLARIN TA webinar mini-walkthrough for data usage in POLARIN!
This notebook demonstrates how to collect and visualize data from POLARIN datasets.

In this notebook, we'll walk through the process of collecting and visualizing data from two POLARIN datasets:
1. Snow Cover Fraction data from the Bayelva area near Ny-Ålesund, Svalbard
2. Meteorological data from the Climate Change Tower in Ny-Ålesund

Let's start by importing the necessary libraries.


```python
import requests
import pandas as pd
import xarray as xr
import io
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")
```

# Step 1: Setting up the data sources
First, we need to specify the URLs for our datasets:


```python
# Dataset 1: Snow Cover in Bayelva area
snow_url = 'https://data.iadc.cnr.it/erddap/griddap/salzano_fractional.nc?fsca%5B(2023-12-31T13:00:01Z):1:(2023-12-31T13:00:01Z)%5D%5B(8761225.0):1:(8765905.0)%5D%5B(430685.0):1:(437395.0)%5D'

# Dataset 2: Weather data from Climate Change Tower
weather_url = 'https://data.iadc.cnr.it/erddap/tabledap/fkvmu3.ncCFMA?time%2Clatitude%2Clongitude%2Cdepth%2CTEMP%2CTEMP_QC%2Cstation_id&time%3E=2023-09-11&time%3C=2025-06-14T00%3A00%3A00Z'
```


# Step 2: Fetch data from the POLARIN GeoNetwork server using ERDDAP/OPeNDAP
This function will help us get data from the POLARIN GeoNetwork server using ERDDAP/OPeNDAP.


```python
snow_ds = xr.open_dataset(snow_url)
weather_ds = xr.open_dataset('weather_url')
```

# Step 3: Fetching metadata for the snow cover dataset
Metadata helps us understand what data is available and how it's structured. Let's take a look at the snow_ds metadata:


```python
snow_ds.attrs
```

... and also the weather_ds metadata:


```python
weather_ds.attrs
```

# Step 4: Checking dimensions of the datasets

To extract only the dimensions, you can do this:


```python
snow_ds.dims
weather_ds.dims
```

# Step 5: Coordinates and Data variables

Variables are where the data or coordinate values are stored. The coordinate variables usually have the same names as their respective dimensions. So to recap, a dimension tells you how many grid points there are, whilst the coordinate variable tells you the values for those grid points. To extract all the coordinate variables at once, we can do this:


```python
snow_ds.coords
weather_ds.coords
```

# WIP: Specifying the time range
We'll fetch data from April 2023 to April 2024:


```python
# Time filters for both datasets
time_filters = '&time%3E=2023-04-29T00%3A00%3A00Z&time%3C=2024-04-29T00%3A00%3A00Z'
```

# WIP: Creating a spatial visualization of Snow Cover Fraction


```python
# WIP: Create a plot of Snow Cover Fraction
print("Creating spatial visualization of Snow Cover Fraction...")
plt.figure(figsize=(10, 6))
plt.scatter(snow_data['longitude'], snow_data['latitude'], c=snow_data['snow_cover_fraction'], cmap='viridis')
plt.colorbar(label='Snow Cover Fraction')
plt.title('Snow Cover Fraction over Bayelva Area (April 2023 - April 2024)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
```

# WIP: Creating a time series visualization of Temperature data


```python
# Create a plot of Temperature data
print("Creating time series visualization of Temperature data...")
plt.figure(figsize=(10, 6))
plt.plot(meteo_data['time'], meteo_data['air_temperature_2m'], label='Air Temperature at 2m')
plt.plot(meteo_data['time'], meteo_data['air_temperature_5m'], label='Air Temperature at 5m')
plt.plot(meteo_data['time'], meteo_data['air_temperature_10m'], label='Air Temperature at 10m')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature at Climate Change Tower (April 2023 - April 2024)')
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent label overlap
plt.show()
```

# Congratulations!

You've successfully fetched and visualized data from two POLARIN datasets. This demonstrates how to:
1. Access data from POLARIN's ERDDAP server
2. Fetch specific variables and time periods
3. Create simple visualizations of the data

You can modify the time range or variables to explore different aspects of these datasets!

| | |
|:-:|:-:|
| <img src="https://ocean-ice.eu/wp-content/uploads/2025/02/TO-USE-RGB-for-digital-materials-V.png" width="160"/> | <img src="https://eu-polarin.eu/wp-content/uploads/2024/04/polarin-web1.svg" width="140"/> |



