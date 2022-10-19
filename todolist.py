def print_menu():
    print("add       : add new task")
    print("done      : close task")
    print("update    : amend task name")
    print("list      : list pending tasks")
    print("list-done : list closed tasks")
    print("list-all  : list all tasks")
    print("quit      : exit the application")


def add_task(list_tasks):
    new_task = (input('Name of task :'), False)
    list_tasks.append(new_task)
    print('task saved ;-)')


def close_task(list_tasks):
    for i, name in enumerate(list_tasks):
        print('tache n°:', i, name[0])
    index_task_to_close = int(input('What task do you want to close?'))

    list_tasks[index_task_to_close] = (list_tasks[index_task_to_close][0], True)
    print('Task closed')


def update_task(list_tasks):
    if len(list_tasks) == 0:
        print('No tasks')
        return

    for i, name in enumerate(list_tasks):
        print('tache n°:', i, name[0])
    index_task_to_update = int(input('What task do you want to update?'))
    new_task_name = input('What is new name of the task?')
    list_tasks[index_task_to_update] = (new_task_name, list_tasks[index_task_to_update][1])
    print('Task name update')


def list_pending_tasks(list_tasks):
    print("List of your pending tasks :")
    for task in list_tasks:
        if not task[1]:
            print(task[0])


def list_done_tasks(list_tasks):
    print("List of your tasks already done :")
    for task in list_tasks:
        if task[1]:
            print(task[0])


def list_all_tasks(list_tasks):
    if len(list_tasks) == 0:
        print('No tasks')
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
            raise Exception('invalid command, please retry')
    except Exception as err:
        print(err)
    finally:
        return list_tasks


def main():
    print('\nWelcome to your To Do List application !\n')
    list_tasks = []
    print_menu()
    user_input = input("Please enter your command :")
    while user_input != "quit":
        list_tasks = do_action(list_tasks, user_input)
        print_menu()
        user_input = input("Please enter your command :")
    print("Goodbye")
    print('╭∩╮(◉_◉)╭∩╮')


if __name__ == "__main__":
    main()
