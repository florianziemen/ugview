from ugview import UGViewer


def test_subset_unstruct_ds(healpix_ds):
    viewer = UGViewer(healpix_ds, "data")
    ds = viewer.subset_unstruct_ds()
    assert ds.equals(healpix_ds.data.isel(time=0))


def test_subset_unstruct_ds_subset(healpix_ds):
    viewer = UGViewer(healpix_ds, "data", subset=dict(time="1"))
    ds = viewer.subset_unstruct_ds()
    assert ds.equals(healpix_ds.data.isel(time=1))


def test_hp_plot(tmp_path, healpix_ds):
    viewer = UGViewer(healpix_ds, "data")
    viewer.plot_field(output=tmp_path / "test.png")


def test_hp_plot_subset(tmp_path, healpix_ds):
    viewer = UGViewer(healpix_ds, "data", subset=dict(time="1"))
    viewer.plot_field(output=tmp_path / "test.png")
