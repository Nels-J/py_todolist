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

    list_tasks[index_task_to_close] = (list_tasks[index_task_to_close][0], False)
    print('Task closed')


def update_task(task):
    if task is None:
        raise Exception("task empty")
    else:
        task = (input('Rename task :'), task[1])
        print('task updated ;-)')
        return task


def list_pending_tasks(task):
    print("List of your pending tasks :")
    if not is_done(task):
        print(task)
    else:
        print('no pending tasks')


def list_done_tasks(task):
    print("List of your closed tasks :")
    if is_done(task):
        print(task)
    else:
        print('no closed tasks')


def is_done(task):
    return task[1]


def list_all_tasks(list_tasks):
    print("List of all your tasks :")
    print(list_tasks)


def do_action(list_tasks, user_input):
    try:
        if user_input == "add":
            add_task(list_tasks)
        elif user_input == "done":
            close_task(list_tasks)
        elif user_input == "update":
            task = update_task(task)
        elif user_input == "list":
            list_pending_tasks(task)
        elif user_input == "list-done":
            list_done_tasks(task)
        elif user_input == "list-all":
            list_all_tasks(list_tasks)
        elif user_input == "quit":
            return
        else:
            raise Exception('invalid command, please retry')
    except Exception as err:
        print(err)
    finally:
        return list_tasks


def main():
    print('\nWelcome to your To Do List application !\n')
    list_tasks = []
    user_input = ""
    while user_input != "quit":
        print_menu()
        user_input = input("Please enter your command :")
        list_tasks = do_action(list_tasks, user_input)
    print("Goodbye")


if __name__ == "__main__":
    main()
