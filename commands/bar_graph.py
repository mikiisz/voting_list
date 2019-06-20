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
            'csv_file_path': ''
        }

        # acceptable arguments
        self.args = {
            '--xaxis': 'xaxis',
            '--xaxis-mode': 'xaxis_mode',
            '--yaxis-left': 'yaxis_left',
            '--yaxis-right': 'yaxis_right',
            '--yaxis-top': 'yaxis_top',
            '--yaxis-bottom': 'yaxis_bottom',
            '--csv-file-path': 'csv_file_path'
        }

        # list of arguments whose can be list
        self.args_can_many = {}
        pass

    def exec_command(self, args):
        self.parse_args(args)
        data_getter = BarGraphDataGetter(self.args_val['csv_file_path'])
        data_getter.set_params(**self.args_val)
        data = data_getter.get_data()
        for key, val in data.items():
            data[key] = val['sum']
        make_bar_graph(data)
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
            'csv_file_path': ''
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
