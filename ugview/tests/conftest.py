import pytest


@pytest.fixture
def healpix_ds():
    import xarray as xr
    import numpy as np

    # Create a sample Healpix dataset
    nside = 4
    npix = 12 * nside**2
    data = np.arange(npix * 2).astype(np.float32).reshape(2, npix)
    time = np.arange(2)

    ds = xr.Dataset(
        {
            "data": (("time", "cell"), data),
            "time": (("time"), time),
        }
    )
    da = xr.DataArray(0)
    da.attrs = dict(grid_mapping_name="healpix", healpix_nside=64, healpix_order="nest")
    ds["crs"] = da
    ds["data"].attrs["grid_mapping"] = "crs"
    ds["data"].attrs["units"] = "1"
    ds["data"].attrs["long_name"] = "Ascending numbers"
    return ds
