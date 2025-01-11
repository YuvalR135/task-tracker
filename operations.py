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

def help_command():
    return "Listing all command options..."

def add_command(task_description):
    return f"Adding task: {task_description}"

def update_command(task_id, task_description):
    return f"Updating task {task_id} with description: {task_description}"

def delete_command(task_id):
    return f"Deleting task {task_id}"

def mark_in_progress_command(task_id):
    return f"Marking task {task_id} as in progress"

def mark_done_command(task_id):
    return f"Marking task {task_id} as done"

def list_command():
    return "Listing all tasks..."

def list_done_command():
    return "Listing all done tasks..."

def list_todo_command():
    return "Listing all todo tasks..."

def list_in_progress_command():
    return "Listing all in-progress tasks..."


def execute_operation(*args):
    operation = args[0]
    if operation in operation_switch:
        func = operation_switch[operation]
        return func(*args)
    else:
        return "Invalid operation"
