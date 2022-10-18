def print_menu():
    print("add       : add new task")
    print("done      : close task")
    print("update    : amend task name")
    print("list      : list pending tasks")
    print("list-done : list closed tasks")
    print("list-all  : list all tasks")
    print("quit      : exit the application")


def add_task():
    task = (input('Name of task :'), False)
    print('task saved ;-)')
    return task


def close_task(task):
    print('Task closed')
    return task[0], True


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


def list_all_tasks(task):
    print("List of all your tasks :")
    if task:
        print(task)
    else:
        print('no tasks')


def do_action(task, user_input):
    try:
        if user_input == "add":
            task = add_task()
        elif user_input == "done":
            task = close_task(task)
        elif user_input == "update":
            task = update_task(task)
        elif user_input == "list":
            list_pending_tasks(task)
        elif user_input == "list-done":
            list_done_tasks(task)
        elif user_input == "list-all":
            list_all_tasks(task)
        else:
            raise Exception('invalid command, please retry')
    except Exception as err:
        print(err)
    finally:
        return task


def main():
    print('\nWelcome to your To Do List application !\n')
    print_menu()
    task: (str, bool) = None
    user_input = input("\nPlease enter your command :")
    while user_input != "quit":
        task = do_action(task, user_input)
        user_input = input("Please enter your command :")
    print("Goodbye")


if __name__ == "__main__":
    main()
