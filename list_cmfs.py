import colour
from colour.plotting import *
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lists the available Color Matching Functions (CMFS)")
    param = parser.parse_args()

    # Load the illuminant
    print("------------------------")
    print("Color Matching Functions")
    print("------------------------")
    for key in colour.MSDS_CMFS:
        print(key)
    