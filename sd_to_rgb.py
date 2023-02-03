import colour
from colour.plotting import *
import matplotlib.pyplot as plt
import numpy as np
import argparse
import json


def sd_to_rgb(in_sd, in_illuminant="E", in_cmfs="CIE 1931 2 Degree Standard Observer", outfile=""):
    # Load the spectral distribution
    if in_sd in colour.SDS_ILLUMINANTS:
        # It is a pre-defined illuminant
        sd = colour.SDS_ILLUMINANTS[in_sd]
    else:
        # Should be a json file...
        with open(in_sd, 'r') as f:
            sd_data = json.load(f)
        # Create the spectral distribution from the sample
        sd = colour.SpectralDistribution(sd_data, name='Input SD')
    
    # Load the CMFS
    if in_cmfs in colour.MSDS_CMFS:
        cmfs = colour.MSDS_CMFS[in_cmfs]
    else:
        raise ValueError("Unknown CMFS type " + in_cmfs + ". Valid types are listed here: https://colour.readthedocs.io/en/develop/generated/colour.MSDS_CMFS.html")

    # Load the illuminant
    if in_illuminant in colour.SDS_ILLUMINANTS:
        illuminant = colour.SDS_ILLUMINANTS[in_illuminant]
    elif in_illuminant in colour.SDS_LIGHT_SOURCES:
        illuminant = colour.SDS_LIGHT_SOURCES[in_illuminant]
    else:
        # Should be a json file...
        with open(out_file, 'w') as f:
            illuminant_data = json.load(f)
        # Create the spectral distribution from the sample
        illuminant = colour.SpectralDistribution(illuminant_data, name='Custom illuminant')

    # Convert to RGB
    sample_xyz = colour.sd_to_XYZ(sd, cmfs, illuminant, method="Integration")    
    sample_rgb = colour.XYZ_to_sRGB(sample_xyz / 100)    

    # Save it, it required to
    if outfile:
        with open(outfile, 'w') as f:
            json.dump(sample_rgb.tolist(), f)

    # Plot everything
    plot_single_sd(sd, standalone=False)
    plot_single_sd(illuminant, standalone=False)
    plot_single_cmfs(cmfs, standalone=False)
    plot_single_colour_swatch(ColourSwatch(sample_rgb, 'Sample'), text_parameters={'size': 'x-large'}, standalone=False)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a spectral distribution to sRGB")
    parser.add_argument('sd', action='store', type=str, help="The spectral distribution (SD) to convert. It can be a path to a JSON file containing the SD samples, or a string with one of the standard illuminants (see the --illuminant parameter below).")
    parser.add_argument('outfile', action='store', type=str, help="The output JSON file where the color will be stored")
    parser.add_argument('--illuminant', action='store', type=str, default="E", help="The illuminant to use. Defaults to the 'E' illuminant (i.e., an all-ones SD), or you can set the path to a JSON file containing the SD samples, or a string with one of the standard illuminants or light sources. You can list the valid types with 'list_illuminants.py'.")
    parser.add_argument('--cmfs', action='store', type=str, default="CIE 1931 2 Degree Standard Observer", help="The colour matching functions (CMFS) to use. Defaults to 'CIE 1931 2 Degree Standard Observer', you can list valid types with 'list_cmfs.py'")
    param = parser.parse_args()

    sd_to_rgb(param.sd, param.illuminant, param.cmfs, param.outfile)