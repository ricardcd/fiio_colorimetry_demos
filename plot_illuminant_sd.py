import colour
from colour.plotting import *
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a spectral distribution to sRGB")
    parser.add_argument('illuminant', action='store', type=str, default="E", help="The illuminant to use. Defaults to the 'E' illuminant (i.e., an all-ones SD), or you can set the path to a JSON file containing the SD samples, or a string with one of the standard illuminants (see the list here: https://colour.readthedocs.io/en/develop/generated/colour.SDS_ILLUMINANTS.html OR https://colour.readthedocs.io/en/develop/generated/colour.SDS_LIGHT_SOURCES.html)")
    param = parser.parse_args()

    # Load the illuminant
    if param.illuminant in colour.SDS_ILLUMINANTS:
        illuminant = colour.SDS_ILLUMINANTS[param.illuminant]
    elif param.illuminant in colour.SDS_LIGHT_SOURCES:
        illuminant = colour.SDS_LIGHT_SOURCES[param.illuminant]

    plot_single_sd(illuminant)