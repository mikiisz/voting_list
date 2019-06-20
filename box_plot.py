import matplotlib.pyplot as plt


def box_plot(title, values):
    _, axs = plt.subplots()
    axs.set_title(title)
    axs.boxplot(values)

    plt.savefig('./graphs/' + title)


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

box_plot('Głosy na nauczycieli', votes_for_teacher)
