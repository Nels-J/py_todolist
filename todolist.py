# from /home/kply/PycharmProjects/py_todolist/Main.py import Main

class Interface:
    def print_menu(self):
        print("add       : add new task")
        print("add2      : add more new task")
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
        "add": ("add new task", "add", add_task),
        #
        # "add2": ("add more new task", "add2", add_task),
        #
        "done2": ("close more task", "done2", close_task),
        #
        "done": ("close task", "done", close_task),
        #
        "update": ("amend task name", "update", update_task),
        #
        "list": ("list pending tasks", "list", list_pending_tasks),
        #
        "list-done": ("list closed tasks", "list-done", list_done_tasks),
        #
        "list-all": ("list all tasks", "list-all", list_all_tasks),

    }
    try:
        actions.get(user_input)[2](list_tasks)

    except Exception as error:
        message_error = 'invalid command, please retry'
        print(error)
    finally:
        return list_tasks


# def main():
#     print('\nWelcome to your To Do List application !\n')
#     list_tasks = []
#     user_input = ""
#     while user_input != "quit":
#         print_menu()
#         user_input = input("Please enter your command :")
#         list_tasks = do_action(list_tasks, user_input)
#     print("Goodbye")
#     print('╭∩╮(◉_◉)╭∩╮')

class Main:
    def __init__(self):
        print("hello")

    @classmethod
    def launch_todolist(cls):
        list_tasks = []
        user_input = ""
        interface = Interface()
        while user_input != "quit":
            interface.print_menu()
            user_input = input("Please enter your command :")
            list_tasks = do_action(list_tasks, user_input)
        print("Goodbye")
        print('╭∩╮(◉_◉)╭∩╮')


if __name__ == "__main__":
    m = Main
    m.launch_todolist()
