from commands.help import Help
from interface_tools.input_tools import *
from commands.bar_graph import BarGraph

bar_graph_command = BarGraph()
help_command = Help()

# load sheet from default location (config.json)

cmd_hist_file = open('commandHistory.txt', 'a+')
user_command_getter = UserCommandGetter(cmd_hist_file)

# program commands
command = {
    "plot-bar-graph": lambda x: bar_graph_command.exec_command(x),
    "help": lambda x: help_command.exec_command(x),
    "exit": lambda x: exit(0),
}


def input_mode():
    # read user input
    args = user_command_getter.get_user_command()
    # args = ['plot-bar-graph', '--yaxis-top', '42']

    if len(args) < 1:
        print("unknown command")
    else:
        if args[0] in command:
            # execute inserted command
            command[args[0]](args)
        else:
            print("unknown command")
    return


def main():
    print("TIMETABLE-GENERATOR WIET 2019 - interactive mode")

    while True:
        input_mode()


if __name__ == "__main__":
    main()