import colour
from colour.plotting import *
import argparse
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot a color stored in a JSON file")
    parser.add_argument('color_file', action='store', help="The JSON file containing the RGB color")
    param = parser.parse_args()

    with open(param.color_file, 'r') as f:
        color_data = json.load(f)

    plot_single_colour_swatch(ColourSwatch(color_data, 'Color'), text_parameters={'size': 'x-large'})