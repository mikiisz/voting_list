import csv
import metadata as md
from collections import OrderedDict


class BarGraphDataGetter:
    XAXIS_VERTICAL = 1
    XAXIS_HORIZONTAL = 2

    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.xaxis = -1
        self.xaxis_mode = -1
        self.yaxis_left = -1
        self.yaxis_right = -1
        self.yaxis_top = -1
        self.yaxis_bottom = -1
        self.count_mode = 0

    def set_params(self, **kwargs):
        for arg in kwargs:
            if arg in self.__dict__:
                self.__dict__[arg] = kwargs[arg]

    def get_data(self):
        return_data = {}
        with open(self.csv_file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            vert_keys = OrderedDict()
            values_matrix = {}
            if self.xaxis_mode == BarGraphDataGetter.XAXIS_VERTICAL:
                if self.xaxis == -1:
                    for _, row in enumerate(csv_reader):
                        for key in row:
                            vert_keys[key] = key
                        break
                else:
                    for row_id, row in enumerate(csv_reader):
                        if row_id != self.xaxis:
                            continue
                        vert_keys = row
                        break
            vert_keys = list(vert_keys.items())
            csv_file.seek(0)
            csv_reader = csv.DictReader(csv_file)

            for row_id, row in enumerate(csv_reader):
                row_list = list(row.items())
                if row_id not in range(self.yaxis_top, self.yaxis_bottom):
                    continue
                for col_id in range(self.yaxis_left, self.yaxis_right):
                    if self.xaxis_mode == BarGraphDataGetter.XAXIS_VERTICAL:
                        if vert_keys[col_id][1] not in values_matrix:
                            values_matrix[vert_keys[col_id][1]] = []
                        if self.count_mode == 0:
                            values_matrix[vert_keys[
                                col_id][1]].append(
                                row_list[col_id][1])
                        else:
                            values_matrix[vert_keys[
                                col_id][1]].append(1)
                    else:
                        if row_list[self.xaxis][1] not in values_matrix:
                            values_matrix[row_list[self.xaxis][1]] = []
                        if self.count_mode == 0:
                            values_matrix[row_list[self.xaxis][1]].append(
                                row_list[col_id][1])
                        else:
                            values_matrix[row_list[self.xaxis][1]].append(1)

        return values_matrix
