import xarray as xr
import logging
import easygems.healpix as egh
import matplotlib.pyplot as plt
from typing import Dict, Union

logger = logging.getLogger(__name__)


class UGViewer:
    def __init__(
        self,
        dataset: xr.Dataset,
        var: str,
        subset: Union[None, Dict[str, str], Dict[str, int]] = None,
    ) -> None:
        self.ds = dataset
        self.var = var
        self.subset = subset or dict()
        logger.critical(self.subset)
        for k, v in self.subset.items():
            self.subset[k] = int(v)

    def plot_hp(self, **kwargs):
        plotvar = self.subset_unstruct_ds()
        return egh.healpix_show(plotvar, **kwargs)

    def subset_unstruct_ds(self):
        plotvar = self.ds[self.var].isel(self.subset)
        if len(dd := plotvar.dims) > 1:
            extra_subset = {x: 0 for x in dd[:-1]}
            logger.warning(
                f"Extra dimensions found in data. Taking first element in each of them: {extra_subset}"
            )
            plotvar = plotvar.isel(extra_subset)
        return plotvar

    def plot_field(self, output=None, **kwargs):
        img = self.plot_hp(**kwargs)
        plt.colorbar(img)
        if output is not None:
            plt.savefig(output)
        else:
            plt.show()
