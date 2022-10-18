def print_menu():
    print("To add a new task, use 'add' command")
    print("To close a task, use 'done' command")
    print("To amend task name, use 'update' command")
    print("To list pending tasks, use 'list' command")
    print("To list closed tasks, use 'list-done' command")
    print("To list all tasks, use 'list-all' command")
    print("To exit the application, use 'quit' command")


def add_task(task):
    task = input('Name of task :')
    print('task saved ;-)')
    return task


def close_task():
    raise Exception("Command under development: please pick another one")


def update_task(task):
    if task == "":
        raise Exception("task empty")
    else:
        task = input('Rename task :')
        print('task updated ;-)')
        return task


def list_pending_tasks():
    raise Exception("Command under development: please pick another one")


def list_done_tasks():
    raise Exception("Command under development: please pick another one")


def list_all_tasks(task):
    print("List of your tasks :")
    print(task)


def main():
    print('\nWelcome to your To Do List application !\n')
    print_menu()
    task: str = ""
    user_input = input("\nPlease enter your command :")
    while user_input != "quit":
        try:
            if user_input == "add":
                task = add_task(task)
            elif user_input == "done":
                close_task()
            elif user_input == "update":
                task = update_task(task)
            elif user_input == "list":
                list_pending_tasks()
            elif user_input == "list-done":
                list_done_tasks()
            elif user_input == "list-all":
                list_all_tasks(task)
            else:
                raise Exception('invalid command, please retry')
        except Exception as err:
            print(err)
        user_input = input("Please enter your command :")
    print("Goodbye")


if __name__ == "__main__":
    main()
