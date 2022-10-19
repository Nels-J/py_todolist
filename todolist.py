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

    def print(self, message):
        print(message)


class NotImplementedException(Exception):
    pass


class InvalidCommandException(Exception):
    pass


class NotIntegerException(Exception):
    pass


class NotInListIndexException(Exception):
    pass


def add_task(list_tasks, interface):
    new_task = (input('Name of task :'), False)
    list_tasks.append(new_task)
    interface.print('task saved ;-)')


def close_task(list_tasks, interface):
    for i, name in enumerate(list_tasks):
        interface.print(f"tache n°: {i} {name[0]}")

    try:
        index_task_to_close = int(input('What task do you want to close?'))
        if index_task_to_close >= len(list_tasks):
            raise NotInListIndexException

        list_tasks[index_task_to_close] = (list_tasks[index_task_to_close][0], True)
        interface.print('Task closed')
    except ValueError:
        try:
            raise NotIntegerException
        except NotIntegerException:
            interface.print("not integer exception")
            close_task(list_tasks, interface)
    except NotInListIndexException:
        interface.print("l'index n'est pas valide")
        close_task(list_tasks, interface)


def update_task(list_tasks, interface):
    if len(list_tasks) == 0:
        interface.print('No tasks')
        return

    for i, name in enumerate(list_tasks):
        interface.print(f"tache n°: {i} {name[0]}")
    try:
        index_task_to_update = int(input('What task do you want to update?'))
        if index_task_to_update >= len(list_tasks):
            raise NotInListIndexException
        new_task_name = input('What is new name of the task?')
        list_tasks[index_task_to_update] = (new_task_name, list_tasks[index_task_to_update][1])
        interface.print('Task name update')
    except ValueError:
        try:
            raise NotIntegerException
        except NotIntegerException:
            interface.print("not integer exception")
            update_task(list_tasks, interface)
    except NotInListIndexException:
        interface.print("l'index n'est pas valide")
        update_task(list_tasks, interface)


def list_pending_tasks(list_tasks, interface):
    interface.print("List of your pending tasks :")
    for task in list_tasks:
        if not task[1]:
            interface.print(task[0])


def list_done_tasks(list_tasks, interface):
    interface.print("List of your tasks already done :")
    for task in list_tasks:
        if task[1]:
            interface.print(task[0])


def list_all_tasks(list_tasks, interface):
    if len(list_tasks) == 0:
        interface.print('No tasks')
        return
    list_done_tasks(list_tasks, interface)
    list_pending_tasks(list_tasks, interface)


def do_action(list_tasks, user_input, interface):
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
        actions.get(user_input)[2](list_tasks, interface)
    except TypeError as e:
        try:
            raise InvalidCommandException
        except InvalidCommandException as error:
            interface.print(e)
    except NotImplementedException as err:
        interface.print("coucou, c'est pas bon")



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


    def launch_todolist(self):
        list_tasks = []
        user_input = ""
        interface = Interface()
        while user_input != "quit":
            interface.print_menu()
            user_input = input("Please enter your command :")
            list_tasks = self.new_do_action(list_tasks, user_input, interface)
        interface.print("Goodbye")
        interface.print('╭∩╮(◉_◉)╭∩╮')

    def new_do_action(self, list_tasks, user_input, interface ):
        actions = {
            "add": ("add new task", "add", self.new_add_task),
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
            actions.get(user_input)[2](list_tasks, interface)
        except TypeError as e:
            try:
                raise InvalidCommandException
            except InvalidCommandException as error:
                interface.print("commande invalide")
        except NotImplementedException as err:
            interface.print("coucou, c'est pas bon")



        finally:
            pass
        return list_tasks

    def new_add_task(self, list_tasks, interface):
        new_task = (input('Name of task :'), False)
        list_tasks.append(new_task)
        interface.print('task saved ;-)')
        return list_tasks


if __name__ == "__main__":
    m = Main()
    m.launch_todolist()
