from mylib.lib import plot_count, plot_scatter, plot_histogram

import matplotlib.pyplot as plt


def save_plot_count(cardio_data):
    plot_count(cardio_data)
    plt.savefig("./results/count.png")


def save_plot_histogram(cardio_data):
    plot_histogram(cardio_data)
    plt.savefig("./results/histogram.png")


def save_plot_scatter(cardio_data):
    plot_scatter(cardio_data)
    plt.savefig("./results/scatter.png")


# if __name__ == "__main__":
#     PATH = "./CardioGoodFitness.csv"
#     save_plot_count(read_dataset(PATH))
