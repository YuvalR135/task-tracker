
from colorama import Fore, Back, Style
from operations import handle_command 


def start_cli():
    print(Fore.GREEN + "Starting task-tracker CLI", end="")
    print(Style.RESET_ALL)
    while True:
        cli_command = input()
        if cli_command == "":
            continue
        if not isinstance(cli_command, str):
            print("Command should be a string")
        
        handle_command(cli_command)
            
        print(Style.RESET_ALL)



def main():
    start_cli()
    
    
if __name__ == "__main__":
    main()