import xarray as xr


def open_data(filename):
    try:
        return xr.open_dataset(filename)
    except ValueError:
        return xr.open_dataset(filename, engine="zarr")
