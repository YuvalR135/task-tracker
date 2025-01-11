from colorama import Fore, Back, Style
import json
from operations import execute_operation

# Define your error codes 
GOOD_COMMAND = "GOOD_COMMAND"
ERROR_MISSING_COMMAND = "ERROR_MISSING_COMMAND"
ERROR_WRONG_ARGS_DATA_TYPES = "ERROR_WRONG_ARGS_DATA_TYPES"
ERROR_WRONG_NUMBER_OF_ARGS = "ERROR_WRONG_NUMBER_OF_ARGS"
ERROR_COMMAND_DOES_NOT_EXISTS = "ERROR_COMMAND_DOES_NOT_EXISTS" 

def operation_name(operation_obj):
    return operation_obj['operation']
    
def read_json():
    with open('commands.json') as commands_file:
        commands_json = json.load(commands_file)
    return commands_json


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
            if len(command_args) - 1 == command['num_of_args']:
                ret = check_data_types(command['args_data_types'], command_args)
                return ret
    return ERROR_WRONG_NUMBER_OF_ARGS


def is_legal_arguments(command_args):
    commands_json = read_json()
    if command_args[0] == 'list' and len(command_args) > 1:
        command_args[0] += f' {command_args[1]}'
        command_args.pop(1)
        print(command_args)
    if command_args[0] in map(operation_name, commands_json):
        ret = check_args(commands_json, command_args):
        if ret == GOOD_COMMAND:
            print("OK")
            return True
        else:
            print(Fore.RED + f"Command task-tracker {command_args[0]} - {ret}.")
    return False


def is_command(command_list):
    if len(command_list) == 1:
        print(Fore.RED + f"Command task-tracker is missing arguments.")
        return
    return is_legal_arguments(command_list[1:])


def handle_command(cli_command):
    command_list = cli_command.split(" ")
    if command_list[0] != "task-tracker":
        print(Fore.RED + f"Command {command_list[0]} is not recognized.")
    elif is_command(command_list):
        print(command_list)
        execute_operation(command_list[1:])
    else:
        print(Fore.RED + f"Command task-tracker is followed by an unknown option.")
        execute_operation(['help'])