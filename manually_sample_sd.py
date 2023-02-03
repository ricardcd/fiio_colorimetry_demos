import colour
import matplotlib
import matplotlib.pyplot as plt
import argparse
import json


def manually_sample_spectral_distribution(out_file):

    print("- Please click the samples of the spectral distribution over the visible spectrum shown on screen (press enter to finish)")
    # plt.ioff()
    # plt.show(block=False)
    fig, ax = colour.plotting.plot_visible_spectrum(standalone=False)
    pts = fig.ginput(-1)
    sd_data = dict((round(x), y) for x, y in pts) # Note the round: the NM must be specified with an int, not a float!
    plt.close(fig)
    
    print("- Showing the sampled spectral distribution, close the window to finish (saving will happend AFTER closing it)")
    sd = colour.SpectralDistribution(sd_data, name='The sampled distribution')
    colour.plotting.plot_single_sd(sd, standalone=True)

    print("- Saving to file")
    with open(out_file, 'w') as f:
        json.dump(sd_data, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Sample a spectral distribution manually over the visible spectrum")
    parser.add_argument('out_file', action='store', type=str, help='The output file where the spectral distribution will be stored')    
    param = parser.parse_args()

    manually_sample_spectral_distribution(param.out_file)