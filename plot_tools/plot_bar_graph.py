import matplotlib.pyplot as plt
import numpy as np


def make_bar_graph(data, title='', xlabel='', ylabel=''):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    data_len = np.arange(len(data))
    ax.barh(data_len, data.values())
    plt.yticks(data_len, data.keys())
    ax.invert_yaxis()
    plt.show()
