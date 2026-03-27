# Making your data FAIR and useful for others

>NOTE: _This section is work in progress!_

## Create a FAIR-compliant datasets from tabular data

This notebook will show you how to transform your tabular data into a FAIR-compliant dataset. First, we should import the neccessary packages.


```python
# Import neccessary packages
import pandas as pd
import xarray as xr
```

---

### Physical, quantitative research data: Create a CF-NetCDF file from tabular data

For this tutorial, we will use exemplary data stored in the `/data` subdirectory under the same parent directory as this notebook. Because not all data is equal (more true would be *all data is not equal*), we will provide guidance on how to go from different kinds of tabular data to FAIR-compliant datasets. 

For this chapter, we will focus on turning your tabular data into CF-NetCDF. The data most suitable to be transformed into this kind of data format is: . This data format is a specific type of NetCDF that is compliant with the Climate and Forecast (CF) metadata conventions (hence *CF*-NetCDF). For more information on the CF metadata conventions, visit their [homepage](https://cfconventions.org/). 

*Note: because CF-NetCDF is only suitable for numerical, quantitative data, this chapter will only provbide examples of non-qualitative datasets. Therefore, this tutorial excludes most ecology and biology-related datasets. For examples on that kind of data, see the chapter `Create a Darwin Core Archive file from tabular data`*!

---

### Qualitative research data: Create a Darwin Core Archive file from tabular data

*Note: because Darwin Core Archive is mostly suited for numerical, quantitative data, this chapter will only provbide examples of non-qualitative datasets. Therefore, this tutorial excludes most ecology and biology-related datasets. For examples on that kind of data, see the chapter `Create a Darwin Core Archive file from tabular data`*!

_Source: [Training Material from NorDataNet (2021)](https://github.com/NorDataNet/TrainingMaterial/tree/71de752803d2fe0e115d53441893106293f87a5c)_
