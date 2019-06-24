import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np


def box_plot(data, title, xlabel, ylabel):
    new_data = OrderedDict()
    max_len = 25
    for key, val in data.items():
        if len(key) > max_len:
            index = max_len - (key[:max_len])[::-1].find(' ')
            key = key[:index - 1] + '\n' + key[index:]
        new_data[key] = list(map(int, val))
    plot_keys = [''] + list(new_data.keys())
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.boxplot(new_data.values(), vert=False)
    plt.yticks(range(len(new_data)+1), plot_keys)
    plt.tight_layout()
    ax.invert_yaxis()
    plt.subplots_adjust(left=0.25)
    plt.show()


# example with 'nauczyciel' copied from .csv
votes_for_teacher = [
    2046,
    800,
    3682,
    1792,
    1498,
    20010,
    587,
    410,
    900,
    1851,
    3266,
    613,
    480,
    2278,
    38052,
    7427,
    64113,
    13576,
    13891,
    27493,
    256,
    10907,
    1868,
    1656,
    393,
    966,
    816,
    13177,
    28610,
    984,
]

# box_plot('Głosy na nauczycieli', votes_for_teacher)
