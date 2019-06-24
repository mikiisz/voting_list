from plot_tools.plot_bar_graph import *
from csv_tools.bar_graph_data import *
from box_plot import box_plot
from statistics import mean
from interface_tools.command_completion_tools import available_expressions


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
            'select_top': -1,
            'count_mode': 0,
            'mode': 'sum',
            'select_key': '',
            'title': 'Wykres',
            'xlabel': 'Oś X',
            'ylabel': 'Oś Y',
            'box_plot': 0
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
            '--select-top': 'select_top',
            '--count-mode': 'count_mode',
            '--mode': 'mode',
            '--select-key': 'select_key',
            '--title': 'title',
            '--xlabel': 'xlabel',
            '--ylabel': 'ylabel',
            '--box-plot': 'box_plot'
        }

        # list of arguments whose can be list
        self.args_can_many = {}
        pass

    def exec_command(self, args):
        self.parse_args(args)
        data_getter = BarGraphDataGetter(self.args_val['csv_file_path'])
        data_getter.set_params(**self.args_val)
        data = data_getter.get_data()
        if self.args_val['select_key'] != '':
            if self.args_val['select_key'] in data:
                data = OrderedDict({self.args_val['select_key']:
                                        data[self.args_val['select_key']]})
            else:
                data = OrderedDict()
        proc_data = {}
        if self.args_val['mode'] == 'mean':
            for key, val in data.items():
                proc_data[key] = {'mean': 0}
                for item in val:
                    proc_data[key]['mean'] = proc_data[key]['mean'] + int(
                        item)
                proc_data[key]['mean'] = proc_data[key]['mean'] / len(val)
            for key, val in proc_data.items():
                proc_data[key] = val['mean']
        if len(proc_data) == 0:
            for key, val in data.items():
                proc_data[key] = {'sum': 0}
                for item in val:
                    try:
                        proc_data[key]['sum'] = proc_data[key]['sum'] + int(
                            item)
                    except:
                        pass
            for key, val in proc_data.items():
                proc_data[key] = val['sum']
        proc_data = OrderedDict(sorted(proc_data.items(), key=lambda
            x: x[1], reverse=True))
        if self.args_val['select_top'] > -1:
            proc_data = OrderedDict(list(proc_data.items())[:self.args_val[
                'select_top']])
        data2 = OrderedDict()
        for key, value in proc_data.items():
            data2[key] = data[key]
        if self.args_val['box_plot'] == 1 or (self.args_val['select_key'] !=
                                              '' and len(data) > 0):
            box_plot(data2, self.args_val['title'], self.args_val[
                'xlabel'], self.args_val['ylabel'])
        else:
            if self.args_val['select_key'] == '':
                make_bar_graph(proc_data, self.args_val['title'], self.args_val[
                    'xlabel'], self.args_val['ylabel'])
        pass

    # parsing input arguments
    def parse_args(self, args):
        self.args_val = {
            'xaxis': -1,
            'xaxis_mode': 'vertical',
            'xaxis_left': -1,
            'yaxis_right': -1,
            'yaxis_top': -1,
            'yaxis_bottom': -1,
            'csv_file_path': '',
            'select_top': -1,
            'count_mode': 0,
            'mode': 'sum',
            'select_key': '',
            'title': 'Wykres',
            'xlabel': 'Oś X',
            'ylabel': 'Oś Y',
            'box_plot': 0
        }

        for i, item in enumerate(args):
            if item in self.args.keys() and i + 1 < len(args):
                if item in self.args_can_many:
                    self.args_val[self.args[item]].append(args[i + 1])
                else:
                    self.args_val[self.args[item]] = args[i + 1]

        for key, val in self.args_val.items():
            if key in ['select_key', 'title', 'xlabel', 'ylabel']:
                self.args_val[key] = val.replace('_', ' ')
            if key in ['csv_file_path', 'mode', 'select_key', 'title', 'xlabel',
                       'ylabel']:
                continue
            if key == 'xaxis_mode':
                self.args_val[key] = available_expressions['plot'][
                    '--xaxis-mode'][val]
                continue
            self.args_val[key] = int(val)
