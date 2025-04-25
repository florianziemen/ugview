#!/usr/bin/env python

import logging

import ugview
from argparser import parse_args

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ugview")


def main():
    args = parse_args()
    kwargs = vars(args).copy()
    for x in ["filename", "var", "subset", "output"]:
        kwargs.pop(x, None)
    ds = ugview.open_data(args.filename)
    ugv = ugview.UGViewer(ds, args.var, args.subset)
    ugv.plot_field(output=args.output, **kwargs)


if __name__ == "__main__":
    main()
