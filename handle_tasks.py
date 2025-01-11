from colorama import Fore, Back, Style
from operations import get_commands, execute_operation

# Define your error codes 
GOOD_COMMAND = "GOOD_COMMAND"
ERROR_MISSING_COMMAND = "ERROR_MISSING_COMMAND"
ERROR_WRONG_ARGS_DATA_TYPES = "ERROR_WRONG_ARGS_DATA_TYPES"
ERROR_WRONG_NUMBER_OF_ARGS = "ERROR_WRONG_NUMBER_OF_ARGS"
ERROR_COMMAND_DOES_NOT_EXISTS = "ERROR_COMMAND_DOES_NOT_EXISTS" 


def operation_name(operation_obj):
    return operation_obj['operation']


def check_data_types(args_data_types, command_args):
    if GOOD_COMMAND == []:
        return True
    else:
        for i in range(len(args_data_types)):
            if args_data_types[i] == 'integer':
                if not command_args[1 + i].isdigit():
                    return ERROR_WRONG_ARGS_DATA_TYPES
    return GOOD_COMMAND


def check_args(commands_json, command_args):
    for command in commands_json:
        if command['operation'] == command_args[0]:
            if len(command_args) - 1 >= command['num_of_args']:
                ret = check_data_types(command['args_data_types'], command_args)
                return ret
    return ERROR_WRONG_NUMBER_OF_ARGS


def is_legal_arguments(command_args):
    commands_json = get_commands()
    if command_args[0] == 'list' and len(command_args) > 1:
        command_args[0] += f' {command_args[1]}'
        command_args.pop(1)
        # print(command_args)
    if command_args[0] == 'add' and len(command_args) > 1:
        command_args[1] = " ".join(command_args[1:])
        command_args = command_args[:2]
        # print(command_args)
        
    if command_args[0] == 'update' and len(command_args) > 2:
        command_args[2] = " ".join(command_args[2:])
        command_args = command_args[:3]    
    
    if command_args[0] in map(operation_name, commands_json):
        # print(command_args)
        ret = check_args(commands_json, command_args)
        if ret == GOOD_COMMAND:
            return command_args
        else:
            print(Fore.RED + f"Command task-tracker {command_args[0]} - {ret}.")
    return False


def is_command(command_list):
    if len(command_list) == 1:
        print(Fore.RED + f"Command task-tracker is missing arguments.")
        return
    return is_legal_arguments(command_list[1:])


def handle_command(cli_command):
    command_list = cli_command.strip().split(" ")
    if command_list[0] != "task-tracker":
        print(Fore.RED + f"Command {command_list[0]} is not recognized.")
    else:
        command_args = is_command(command_list)
        if command_args:
            execute_operation(command_args)
        else:        
            print(Fore.RED + f"Command task-tracker is followed by an unknown option.")
            execute_operation(['help'])