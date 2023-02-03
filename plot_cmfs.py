import colour
from colour.plotting import *
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot a given CMFS")
    parser.add_argument('cmfs', action='store', type=str, default="E", help="The illuminant to use. Defaults to the 'E' illuminant (i.e., an all-ones SD), or you can set the path to a JSON file containing the SD samples, or a string with one of the standard illuminants (see the list here: https://colour.readthedocs.io/en/develop/generated/colour.SDS_ILLUMINANTS.html OR https://colour.readthedocs.io/en/develop/generated/colour.SDS_LIGHT_SOURCES.html)")
    param = parser.parse_args()

    # Load the CMFS
    if param.cmfs in colour.MSDS_CMFS:
        cmfs = colour.MSDS_CMFS[param.cmfs]
    else:
        raise ValueError("Unknown CMFS type " + param.cmfs + ". You can list the available types with 'list_cmfs.py'.")

    # Plot it
    plot_single_cmfs(cmfs)
    