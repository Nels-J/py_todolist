print('\nWelcome to your To Do List application !\n')


def print_menu():
    print("To add a new task, use 'add' command")
    print("To close a task, use 'done' command")
    print("To amend task name, use 'update' command")
    print("To list pending tasks, use 'list' command")
    print("To list closed tasks, use 'list-done' command")
    print("To list all tasks, use 'list-all' command")
    print("To exit the application, use 'quit' command")


def user_input():
    new_command = input("\nPlease enter your command :")
    try:
        validate_command(new_command)
    except Exception as err:
        print(err)
        print_menu()
        user_input()


def quit():
    print("\nGoodbye\n")


def validate_command(new_command):
    if new_command == "quit":
        quit()
    elif new_command == "add" or new_command == "done" or new_command == "update" or new_command == "list" or new_command == "list-done" or new_command == "list-all":
        raise Exception("\nCommand under development: please pick another one\n")
    else:
        raise Exception('\ninvalid command, please retry\n')


print_menu()
user_input()
