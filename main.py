
from colorama import Fore, Back, Style
from handle_tasks import handle_command 


def start_cli():
    print(Fore.GREEN + "Starting task-tracker CLI")
    print(Style.RESET_ALL, end="")
    while True:
        print(">>>>>>>> ", end="")
        cli_command = input()
        if cli_command == "":
            continue
        if not isinstance(cli_command, str):
            print("Command should be a string")
        
        handle_command(cli_command)
            
        print(Style.RESET_ALL, end="")



def main():
    start_cli()
    
    
if __name__ == "__main__":
    main()