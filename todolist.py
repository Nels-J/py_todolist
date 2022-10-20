from exceptions import NotInListIndexException, NotIntegerException, NotImplementedException, InvalidCommandException
from tasksList import TasksList

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

def add_task(list_tasks, interface):
    new_task = (input('Name of task :'), False)
    list_tasks.append(new_task)
    interface.print('task saved ;-)')


# def close_task(list_tasks, interface):
#     for i, name in enumerate(list_tasks):
#         interface.print(f"tache n°: {i} {name[0]}")
#
#     try:
#         index_task_to_close = int(input('What task do you want to close?'))
#         if index_task_to_close >= len(list_tasks):
#             raise NotInListIndexException
#
#         list_tasks[index_task_to_close] = (list_tasks[index_task_to_close][0], True)
#         interface.print('Task closed')
#     except ValueError:
#         try:
#             raise NotIntegerException
#         except NotIntegerException:
#             interface.print("not integer exception")
#             close_task(list_tasks, interface)
#     except NotInListIndexException:
#         interface.print("l'index n'est pas valide")
#         close_task(list_tasks, interface)


class Main:

    def __init__(self):
        pass


    def launch_todolist(self):
        list_tasks = TasksList()
        user_input = ""
        interface = Interface()
        while user_input != "quit":
            interface.print_menu()
            user_input = input("Please enter your command :")
            list_tasks = self.do_action(list_tasks, user_input, interface)
        interface.print("Goodbye")
        interface.print('╭∩╮(◉_◉)╭∩╮')

    def do_action(self, list_tasks, user_input, interface):
        actions = {
            "add": ("add new task", "add", list_tasks.add_task),

            "done": ("close task", "done", list_tasks.close_task),
            #
            "update": ("amend task name", "update", list_tasks.update_task),
            #
            "list": ("list pending tasks", "list", list_tasks.list_pending_tasks),
            #
            "list-done": ("list closed tasks", "list-done", list_tasks.list_done_tasks),
            #
            "list-all": ("list all tasks", "list-all", list_tasks.list_all_tasks),

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



if __name__ == "__main__":
    m = Main()
    m.launch_todolist()
