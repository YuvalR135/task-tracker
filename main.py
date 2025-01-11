
from colorama import Fore, Back, Style
import json
from operations import operation

commands_list = ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']

def start_cli():
    while True:
        cli_command = input()
        if cli_command == "":
            continue
        if not isinstance(cli_command, str):
            print("Command should be a string")
        
        command_list = cli_command.split(" ")
        if command_list[0] != "task-tracker":
            print(Fore.RED + f"Command {command_list[0]} is not recognized.", end="\n")
        elif len(command_list) > 1:
            if command_list[1] == "help":
                help()
            elif command_list[1] in command_list:
                operation(command_list)
            else:
                print(Fore.RED + f"Command task-tracker is followed by unknown option.", end="\n")
                help()
            
            
        print(Style.RESET_ALL)



    
def main():
    print('Hi')
    start_cli()
    
    
if __name__ == "__main__":
    main()