from interface_tools.getch import _Getch
from interface_tools.output_tools import *
from interface_tools.command_completion_tools import *
import sys
import os

# getting terminal width and height (in characters) for displaying command
# line correctly
tty_rows, tty_columns = os.popen('stty size', 'r').read().split()
tty_rows = int(tty_rows)
tty_columns = int(tty_columns)


class UserCommandGetter:
    # class of user command getter that provides user command string split,
    # with additional command auto-completion and command history

    def __init__(self, cmd_hist_file):
        self.getch = _Getch()
        self.user_command = ''
        self.cur_user_command = ''
        self.cmd_hist_file = cmd_hist_file
        self.cursor_pos = 0

    # switches to command line mode with command auto-completion and handling
    # special keys, returns command string split after '\n' receiving
    def get_user_command(self):
        # preparing do run command line
        self.user_command = ''
        self.cur_user_command = ''
        self.cmd_hist_file.seek(0)
        cmd_hist = self.cmd_hist_file.readlines()
        hist_cmd_id = 0
        self.cursor_pos = 0
        self.cur_cursor_pos = 0

        # get one key from keyboard
        ret_val = self.get_next_char()

        # run until '\n' character is received
        while ret_val != 0:

            # move cursor during receiving new normal character
            if ret_val == 1:
                self.cursor_pos += 1

            # up arrow handler - previous command from history
            if ret_val == 3:
                if hist_cmd_id < len(cmd_hist):
                    hist_cmd_id += 1
                    self.user_command = cmd_hist[-hist_cmd_id][0:-1]
                    self.cursor_pos = len(self.user_command)

            # down arrow handler - next command from history
            if ret_val == 4:
                if hist_cmd_id > 0:
                    hist_cmd_id -= 1
                    if hist_cmd_id == 0:
                        self.user_command = self.cur_user_command
                        self.cursor_pos = self.cur_cursor_pos
                    else:
                        self.user_command = cmd_hist[-hist_cmd_id][0:-1]
                        self.cursor_pos = len(self.user_command)

            # tab key handler - run command auto-completion
            if ret_val == 5:
                command_completion = complete_command(
                    self.user_command[:self.cursor_pos])
                self.user_command = self.user_command[:self.cursor_pos] + \
                                    command_completion + self.user_command[
                                                         self.cursor_pos:]
                self.cursor_pos += len(command_completion)

            # right arrow handler - move cursor
            if ret_val == 6:
                if self.cursor_pos < len(self.user_command):
                    self.cursor_pos += 1

            # left arrow handler - move cursor
            if ret_val == 7:
                if self.cursor_pos > 0:
                    self.cursor_pos -= 1

            # remember currently provided command (in case go to history)
            if hist_cmd_id == 0:
                self.cur_user_command = self.user_command
                self.cur_cursor_pos = self.cursor_pos

            # get one key from keyboard
            ret_val = self.get_next_char()

        # leave current terminal line
        print()
        self.cmd_hist_file.write(self.user_command + '\n')
        self.cmd_hist_file.flush()
        return self.user_command.split()

    # do some action with command string and returns specific value that
    # depends on pressed key
    def get_next_char(self):
        # clear current line and show command prompt with current command string
        print('\r', ' ' * (tty_columns - 2), '\r', end='')
        show_prompt()
        print(self.user_command, end='')

        # move terminal cursor to right position (in case editing)
        print((len(self.user_command) - self.cursor_pos) * '\b', end='')

        # forced flush whole content to terminal
        sys.stdout.flush()

        # wait for new key press
        cur_char = self.getch.__call__()

        # if ENTER key pressed
        if cur_char == chr(13):
            return 0

        # if BACKSPACE key pressed
        if cur_char == chr(127):
            if self.cursor_pos > 0:
                self.user_command = self.user_command[:self.cursor_pos - 1] + \
                                    self.user_command[self.cursor_pos:]
                self.cursor_pos -= 1
            return 2

        # if DELETE key pressed
        if cur_char == chr(126):
            if self.cursor_pos < len(self.user_command):
                self.user_command = self.user_command[:self.cursor_pos] + \
                                    self.user_command[self.cursor_pos + 1:]
            return 2

        # if ARROW pressed - this press always with following 2 keys
        if cur_char == chr(27):
            # gets extra keys from input buffer
            extra1 = self.getch.__call__()
            extra2 = self.getch.__call__()

            # if UP ARROW pressed
            if extra1 == '[' and extra2 == 'A':
                return 3

            # if DOWN ARROW pressed
            if extra1 == '[' and extra2 == 'B':
                return 4

            # if RIGHT ARROW pressed
            if extra1 == '[' and extra2 == 'C':
                return 6

            # if LEFT ARROW pressed
            if extra1 == '[' and extra2 == 'D':
                return 7

            # other, unhandled special key pressed
            return -1

        # if TAB key pressed
        if cur_char == '\t':
            return 5

        # if CTRL+C key combination pressed => generates exit command
        if cur_char == chr(3):
            self.user_command = 'exit'
            return 0

        # normal key pressed => add character to string in cursor position
        self.user_command = self.user_command[:self.cursor_pos] + \
                            cur_char + self.user_command[self.cursor_pos:]
        return 1
