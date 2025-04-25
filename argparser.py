import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Plot Healpix data")
    parser.add_argument("filename", type=str, help="Path to the data file")
    parser.add_argument("var", type=str, help="Variable to plot")
    parser.add_argument(
        "--subset",
        action=ParseKwargs,
        default=None,
        help="Subset to plot (optional)",
        nargs="+",
    )
    parser.add_argument(
        "--vmin", type=float, default=None, help="Minimum value for color scale"
    )
    parser.add_argument(
        "--vmax", type=float, default=None, help="Maximum value for color scale"
    )
    parser.add_argument(
        "--output", "-o", type=str, default=None, help="Output file name"
    )

    args = parser.parse_args()
    return args


class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split("=")
            getattr(namespace, self.dest)[key] = value
