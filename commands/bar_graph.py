from plot_tools.plot_bar_graph import *
from csv_tools.bar_graph_data import *


class BarGraph:

    def __init__(self):
        # container for arguments
        self.args_val = {
            'xaxis': -1,
            'xaxis_mode': -1,
            'xaxis_left': -1,
            'yaxis_right': -1,
            'yaxis_top': -1,
            'yaxis_bottom': -1,
            'csv_file_path': '',
            'select_top': -1
        }

        # acceptable arguments
        self.args = {
            '--xaxis': 'xaxis',
            '--xaxis-mode': 'xaxis_mode',
            '--yaxis-left': 'yaxis_left',
            '--yaxis-right': 'yaxis_right',
            '--yaxis-top': 'yaxis_top',
            '--yaxis-bottom': 'yaxis_bottom',
            '--csv-file-path': 'csv_file_path',
            '--select-top': 'select_top'
        }

        # list of arguments whose can be list
        self.args_can_many = {}
        pass

    def exec_command(self, args):
        self.parse_args(args)
        data_getter = BarGraphDataGetter(self.args_val['csv_file_path'])
        data_getter.set_params(**self.args_val)
        data = data_getter.get_data()
        summed_data = {}
        for key, val in data.items():
            summed_data[key] = {'sum': 0}
            for item in val:
                summed_data[key]['sum'] = summed_data[key]['sum'] + int(
                    item)
        for key, val in summed_data.items():
            summed_data[key] = val['sum']
        summed_data = OrderedDict(sorted(summed_data.items(), key=lambda
            x: x[1], reverse=True))
        if self.args_val['select_top'] > -1:
            summed_data = OrderedDict(list(summed_data.items())[:self.args_val[
                'select_top']])
        make_bar_graph(summed_data)
        pass

    # parsing input arguments
    def parse_args(self, args):
        self.args_val = {
            'xaxis': -1,
            'xaxis_mode': -1,
            'xaxis_left': -1,
            'yaxis_right': -1,
            'yaxis_top': -1,
            'yaxis_bottom': -1,
            'csv_file_path': '',
            'select_top': -1
        }

        for i, item in enumerate(args):
            if item in self.args.keys() and i + 1 < len(args):
                if item in self.args_can_many:
                    self.args_val[self.args[item]].append(args[i + 1])
                else:
                    self.args_val[self.args[item]] = args[i + 1]

        for key, val in self.args_val.items():
            if key == 'csv_file_path':
                continue
            self.args_val[key] = int(val)
