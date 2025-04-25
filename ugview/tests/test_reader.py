import pytest
from ugview import open_data


@pytest.fixture
def nc_file(tmp_path, healpix_ds):
    # Create a temporary file with the dataset
    data_file = tmp_path / "test_data.nc"
    healpix_ds.to_netcdf(data_file)
    return data_file


@pytest.fixture
def zarr_file(tmp_path, healpix_ds):
    # Create a temporary file with the dataset
    data_file = tmp_path / "test_data.zarr"
    healpix_ds.to_zarr(data_file)
    return data_file


@pytest.fixture
def hidden_zarr_file(tmp_path, healpix_ds):
    # Create a temporary file with the dataset
    data_file = tmp_path / "test_data"
    healpix_ds.to_zarr(data_file)
    return data_file


def test_nc(healpix_ds, nc_file):
    ds = open_data(nc_file)
    assert healpix_ds.identical(ds)


def test_zarr(healpix_ds, zarr_file):
    ds = open_data(zarr_file)
    assert healpix_ds.identical(ds)


def test_hidden_zarr(healpix_ds, hidden_zarr_file):
    ds = open_data(hidden_zarr_file)
    assert healpix_ds.identical(ds)


def test_open_data_invalid_file(tmp_path):
    invalid_file = tmp_path / "invalid_data.txt"
    with open(invalid_file, "w") as f:
        f.write("This is not a valid dataset.")
    with pytest.raises(ValueError):
        open_data(invalid_file)


def test_open_data_missing_file(tmp_path):
    missing_file = tmp_path / "missing_data.nc"
    with pytest.raises(FileNotFoundError):
        open_data(missing_file)
