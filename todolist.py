from Interface import Interface
from InvalidCommandException import InvalidCommandException
from Task import Task


def add_task(list_tasks):
    new_task = Task(interface.input('Name of task :'))
    list_tasks.append(new_task)
    interface.print('task saved ;-)')


def close_task(list_tasks):
    for i, task in enumerate(list_tasks):
        interface.print(f'tache n°: {i} {task.name}')
    index_task_to_close = int(interface.input('What task do you want to close?'))
    task = list_tasks[index_task_to_close]
    task.done()
    interface.print('Task closed')


def update_task(list_tasks):
    if len(list_tasks) == 0:
        interface.print('No tasks')
        return

    for i, task in enumerate(list_tasks):
        interface.print(f'tache n°: {i} {task.name}')

    index_task_to_update = int(interface.input('What task do you want to update?'))
    new_task_name = interface.input('What is new name of the task?')
    task = list_tasks[index_task_to_update]
    task.update(new_task_name)
    interface.print('Task name update')


def list_pending_tasks(list_tasks):
    interface.print("List of your pending tasks :")
    for task in list_tasks:
        if not task.status:
            interface.print(task.name)


def list_done_tasks(list_tasks):
    interface.print("List of your tasks already done :")
    for task in list_tasks:
        if task.status:
            interface.print(task.name)


def list_all_tasks(list_tasks):
    if len(list_tasks) == 0:
        interface.print('No tasks')
        return
    list_done_tasks(list_tasks)
    list_pending_tasks(list_tasks)


def do_action(list_tasks, user_input):
    actions = {
        "add": ('add new task', add_task),
        "done": ('close task', close_task),
        "update": ('amend task name', update_task),
        "list": ('list pending tasks', list_pending_tasks),
        "list-done": ('list closed tasks', list_done_tasks),
        "list-all": ('list_all_tasks', list_all_tasks),
    }
    try:
        if user_input in actions.keys():
            label, action = actions.get(user_input)
            action(list_tasks)
        else:
            raise InvalidCommandException()
    except InvalidCommandException:
        print("La commande est invalide")
    finally:
        return list_tasks


def main():
    interface.print('\nWelcome to your To Do List application !\n')
    list_tasks = []
    interface.print_menu()
    user_input = interface.input("Please enter your command :")
    while user_input != "quit":
        list_tasks = do_action(list_tasks, user_input)
        interface.print_menu()
        user_input = interface.input("Please enter your command :")
    interface.print("Goodbye ╭∩╮(◉_◉)╭∩╮")


if __name__ == "__main__":
    interface = Interface()
    main()
