import json
import os

task_file_path = 'tasks.json'

def read_json(file_path): 
    if os.path.exists(file_path): 
        with open(file_path, 'r') as file: 
            content = file.read() 
            if content.strip(): # Check if file is not empty or contains only whitespace 
                data = json.loads(content) 
            else: 
                data = {} # Initialize with an empty dictionary if file is empty 
    else: 
        data = {} # Initialize with an empty dictionary if file does not exist
    return data


def write_json(file_path, data):
    json_data = json.dumps(data, indent=4, default=str)
    with open(file_path, 'w') as file:
        file.write(json_data)


def get_next_id(data):
    if data:
        return int(max(map(int, data.keys()))) + 1
    else:
        return 1


def is_task_id_exists(data, task_id):
    if data != {}:
        return task_id in data.keys()
    return False


def is_there_any_tasks(data, status):
    if data == {}:
        return False
    elif not status:
        return data != {}
    else:
        for id, task in data.items():
            if task['status'] == status:
                return True
    return False


def get_commands():
    with open('commands.json') as commands_file:
        commands_json = json.load(commands_file)
    return commands_json


def print_task(task_id, task):
    print(f"Task id {task_id}:")
    for key, value in task.items():
        print(f"\t {key} : {value}")


def help_command():
    commands_json = get_commands()
    print('****** task-tracker command options: ******')
    for command in commands_json:
        print(command['operation'])
        print('\t' + command['description'])


def add_command(args):
    from datetime import datetime
    task_description = args[0]
    data = read_json(task_file_path)
    id = get_next_id(data)
    data[id] = {'desc': task_description, 'status': 'todo',
                'createdAt': datetime.now(), 'changedAt': datetime.now()}
    write_json(task_file_path, data)


def update_command(task_args):
    from datetime import datetime
    task_id, task_description = task_args
    data = read_json(task_file_path)
    if not is_task_id_exists(data, task_id):
        print("Task id does not exists in list.")
        return
    data[task_id]['desc'] = task_description
    data[task_id]['changedAt'] = datetime.now()
    write_json(task_file_path, data)


def delete_command(args):
    task_id = args[0]
    data = read_json(task_file_path)
    if not is_task_id_exists(data, task_id):
        print("Task id does not exists in list.")
        return
    del data[task_id]
    write_json(task_file_path, data)


def mark_in_progress_command(args):
    task_id = args[0]
    data = read_json(task_file_path)
    if not is_task_id_exists(data, task_id):
        print("Task id does not exists in list.")
        return
    data[task_id]['status'] = 'in-progress'
    write_json(task_file_path, data)


def mark_done_command(args):
    task_id = args[0]
    data = read_json(task_file_path)
    if not is_task_id_exists(data, task_id):
        print("Task id does not exists in list.")
        return
    data[task_id]['status'] = 'done'
    write_json(task_file_path, data)


def list_command():
    data = read_json(task_file_path)
    if not is_there_any_tasks(data, None):
        print("There are currently no tasks")
        return
    print("Displaying all tasks:")
    for task_id, task in data.items():
        print_task(task_id, task)


def list_done_command():
    data = read_json(task_file_path)
    if not is_there_any_tasks(data, 'done'):
        print("There are currently no done tasks")
        return
    print("Displaying all done tasks:")
    for task_id, task in data.items():
        if task['status'] == 'done':
            print_task(task_id, task)


def list_todo_command():
    data = read_json(task_file_path)
    if not is_there_any_tasks(data, 'todo'):
        print("There are currently no todo tasks")
        return
    print("Displaying all todo tasks:")
    for task_id, task in data.items():
        if task['status'] == 'todo':
            print_task(task_id, task)


def list_in_progress_command():
    data = read_json(task_file_path)
    if not is_there_any_tasks(data, 'in-progress'):
        print("There are currently no in-progress tasks")
        return
    print("Displaying all in-progress tasks:")
    for task_id, task in data.items():
        if task['status'] == 'in-progress':
            print_task(task_id, task)


operation_switch = {
    "help": help_command,
    "add": add_command,
    "update": update_command,
    "delete": delete_command,
    "mark-in-progress": mark_in_progress_command,
    "mark-done": mark_done_command,
    "list": list_command,
    "list done": list_done_command,
    "list todo": list_todo_command,
    "list in-progress": list_in_progress_command,
}

def execute_operation(args):
    operation = args[0]
    if len(args) == 1:
        command_args = None
    else:
        command_args = args[1:]
    # print(operation)
    
    if operation in operation_switch:
        func = operation_switch[operation]
        # print(command_args)
        if not command_args:
            func()
        else:
            func(command_args)
    else:
        return "Invalid operation"
