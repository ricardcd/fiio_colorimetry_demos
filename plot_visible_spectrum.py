from colour.plotting import *
import matplotlib
import matplotlib.pyplot as plt
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plots the visible spectrum")
    param = parser.parse_args()

    fig, ax = plot_visible_spectrum()