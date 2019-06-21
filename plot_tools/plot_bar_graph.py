import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict


def make_bar_graph(data, title='', xlabel='', ylabel=''):
    new_data = OrderedDict()
    max_len = 25
    for key, val in data.items():
        if len(key) > max_len:
            index = max_len - (key[:max_len])[::-1].find(' ')
            key = key[:index - 1] + '\n' + key[index:]
        new_data[key] = val
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    data_len = np.arange(len(new_data))
    ax.barh(data_len, new_data.values())
    plt.yticks(data_len, new_data.keys())
    ax.invert_yaxis()
    plt.show()
