import xarray as xr


def open_data(filename):
    try:
        return xr.open_dataset(filename)
    except ValueError as ve:
        try:
            return xr.open_dataset(filename, engine="zarr")
        except Exception:
            raise ValueError(
                f"Cannot open file {filename} as a dataset. Also tried engine='zarr' explicitly."
            ) from ve
