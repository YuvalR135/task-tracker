from colorama import Fore, Back, Style
import json

def operation_name(operation_obj):
    return operation_obj['operation']
    
def read_json():
    with open('commands.json') as commands_file:
        commands_json = json.load(commands_file)
    return commands_json


def check_data_types(args_data_types, command_args):
    if args_data_types == []:
        return True
    else:
        for i in range(len(args_data_types)):
            if args_data_types[i] == 'integer':
                if not command_args[1 + i].isdigit():
                    return False
    return True


def check_args(commands_json, command_args):
    for command in commands_json:
        if command['operation'] == command_args[0]:
            if len(command_args) - 1 == command['num_of_args']:
                if check_data_types(command['args_data_types'], command_args):
                    return True
    return False


def is_legal_argument(command_args):
    commands_json = read_json()
    if command_args[0] == 'list' and len(command_args) > 1:
        command_args[0] += f' {command_args[1]}'
        command_args.pop(1)
        print(command_args)
    if command_args[0] in map(operation_name, commands_json):
        if check_args(commands_json, command_args):
            print("OK")
            # operation(command_args)
        else:
            print(Fore.RED + f"Command task-tracker {command_args[0]} have wrong arguments.")
    print(2)


def is_command(command_list):
    if len(command_list) == 1:
        print(Fore.RED + f"Command task-tracker is missing arguments.")
    else:
        if is_legal_argument(command_list[1:]):
            print(5)
        
        
    print(Fore.RED + f"Command task-tracker is followed by an unknown option.")
    return False


def operation():
    return


def handle_command(cli_command):
    command_list = cli_command.split(" ")
    if command_list[0] != "task-tracker":
        print(Fore.RED + f"Command {command_list[0]} is not recognized.")
    if is_command(command_list):
        print(command_list)
        operation(command_list[1:])
    # else:
    #     print(Fore.RED + f"Command task-tracker is followed by an unknown option.")
    #     operation(['help'])