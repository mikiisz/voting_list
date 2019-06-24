
# recursive dictionary with available expression used as command
# auto-completion expressions list: first level - command names; second level
# - flags names, third level - available values for particular flags
available_expressions = {
    "plot": {
        '--xaxis': {},
        '--xaxis-mode': {'vertical': 1, 'horizontal': 2},
        '--yaxis-left': {},
        '--yaxis-right': {},
        '--yaxis-top': {},
        '--yaxis-bottom': {},
        '--csv-file-path': {},
        '--select-top': {},
        '--count-mode': {'0': 0, '1': 1},
        '--mode': {'sum': 0, 'mean': 1},
        '--select-key': {},
        '--title': {},
        '--xlabel': {},
        '--ylabel': {},
        '--box-plot': {'0': 0, '1': 1}
    },
    "help": {},
    "exit": {}
}


# run command auto-completion algorithm and returns postfix of last word,
# if it is only one expression from list with the provided prefix;
# in other case show all possible endings of last expression
def search_completion_from_dict(current_expression, expr_dict):
    cmd_len = len(current_expression)
    found_key = None
    more_keys_found = False
    # search for all records of provided dictionary
    for key, value in expr_dict.items():
        # if current expression matches to last expression
        if key[0: cmd_len] == current_expression:
            if found_key is None:
                found_key = key
            else:
                if not more_keys_found:
                    # start showing possible endings of last expression
                    print('\n', found_key, end='')
                    more_keys_found = True

                # add next possible endings
                print('    ', key, end='')
                found_key = longestSubstringFinder(found_key, key)

    # finish showing possible endings
    if more_keys_found:
        print()

    # if no expression matches to last expression
    if found_key is None:
        return ''
    else:
        # return rest of the found expression
        return_str = found_key[cmd_len:]

        # if it is only one expression => add extra space after expression
        if not more_keys_found:
            return_str += ' '
        return return_str


# process provided string and run with it command auto-completion
def complete_command(current_command):
    cmd_split_len = len(current_command.split())

    # if no valid command name in provided string
    if cmd_split_len == 0 or (cmd_split_len == 1 and
                              current_command.split()[0] not in
                              available_expressions):
        return search_completion_from_dict(current_command,
                                           available_expressions)
    rest_expr = current_command.split()[1:]
    command = current_command.split()[0]

    # if invalid command provided
    if command not in available_expressions:
        return ''

    # if command string contains valid command name and doesn't contain space
    # at the end of string
    if len(rest_expr) == 0 and current_command[-1] != ' ':
        return ' '
    expected_flag = True
    cur_flag = None

    # iterate over all words in rest of string
    while len(rest_expr) > 0:
        space_at_end = True

        # if no space at the end of provided string
        if len(rest_expr) == 1:
            if current_command[-1] != ' ':
                space_at_end = False

        # next word must be a flag
        if expected_flag:
            cur_flag = rest_expr[0]

            # if flag is in list of flags for particular command
            if cur_flag in available_expressions[command] and space_at_end:
                expected_flag = False
        # next word must be a flag value
        else:
            cur_key = rest_expr[0]
            # if flag value is in list of values of particular flag; or in
            # case empty list of values => if any value provided
            if (cur_key in available_expressions[command][
                cur_flag] or len(available_expressions[command][
                                     cur_flag]) == 0) and space_at_end:
                expected_flag = True
                cur_flag = None

        # if it is last word of string
        if len(rest_expr) == 1:
            break
        else:
            # make new list from current list without currently processed word
            rest_expr = rest_expr[1:]

    # if next expression should be a flag => run command auto-completion with
    # providing dictionary of flags
    if expected_flag:
        # if no flag name part is provided
        if len(rest_expr) == 0:
            return search_completion_from_dict('',
                                               available_expressions[command])
        else:
            cur_expr = rest_expr[0]
            if cur_expr[0] != '-':
                cur_expr = ''
            return search_completion_from_dict(cur_expr,
                                               available_expressions[command])
    # if next expression should be a flag value => run command
    # auto-completion with providing dictionary of flag values (if not empty)
    else:
        cur_expr = rest_expr[0]
        # if list of flag values is empty => no command auto-completion
        if len(available_expressions[command][cur_flag]) == 0:
            if cur_expr in available_expressions[command]:
                return ''
            else:
                return ' '
        else:
            if cur_expr in available_expressions[command]:
                cur_expr = ''
            return search_completion_from_dict(cur_expr,
                                               available_expressions[command][
                                                   cur_flag])


# returns common beginning substring of two strings
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        if i < len2:
            if string1[i] == string2[i]:
                answer += string1[i]
            else:
                break
        else:
            break
    return answer
