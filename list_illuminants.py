import colour
from colour.plotting import *
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lists the available illuminants")
    param = parser.parse_args()

    # Load the illuminant
    print("--------------------")
    print("Standard illuminants")
    print("--------------------")
    for key in colour.SDS_ILLUMINANTS:
        print(key)
    print("")
    print("-------------")
    print("Light sources")
    print("-------------")
    for key in colour.SDS_LIGHT_SOURCES:
        print(key)
    