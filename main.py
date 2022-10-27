from Exceptions.NotAnIntException import NotAnIntException
from Exceptions.MenuEntryDoesNotExist import MenuEntryDoesNotExist
from Interface import Interface
from Task import Task
from TasksList import TasksList


class Application:
    def __init__(self):
        self.interface = Interface()
        pass

    def launch(self):
        menu = {"add": ("Ajouter une tâche", self.add),
                "close": ("Terminer une tâche", self.close),
                "update": ("Modifier le libellé d'une tâche", self.update),
                "list": ("Lister les tâches en cours", self.list),
                "list-done": ("Lister les tâches terminées", self.list_done),
                "list-all": ("Lister toutes les tâches", self.list_all),
                "test": ("test", self.scenario)
                }
        self.interface.print_menu(menu)
        action = user_choice = self.interface.ask_action()
        while action != "quit":
            self.user_command(user_choice, menu)
            action = user_choice = self.interface.ask_action()
        self.interface.goodbye()

    def user_command(self, user_choice, menu):
        try:
            if user_choice in menu.keys():
                menu[user_choice][1]()
            else:
                raise MenuEntryDoesNotExist()
        except MenuEntryDoesNotExist:
            self.interface.menu_entry_does_not_exist()

    def scenario(self):
        tasks.add(Task('t1'))
        tasks.add(Task('T2'))
        tasks.list[0].update('new t1')
        tasks.list[1].close()
        self.list_all()

    def list(self):
        pending_tasks = tasks.list_according_to_status(False)
        if len(pending_tasks) > 0:
            self.interface.undone_tasks_are()
            for pending_task in pending_tasks:
                self.interface.display_task_with_nb(pending_task)
        else:
            self.interface.no_undone_task()

    def list_done(self):
        done_tasks = tasks.list_according_to_status(True)
        if len(done_tasks) > 0:
            self.interface.done_tasks_are()
            for done_task in done_tasks:
                self.interface.display_task_with_nb(done_task)
        else:
            self.interface.no_done_task()

    def list_all(self):
        self.list()
        self.list_done()

    def add(self):
        user_task = self.interface.ask_new_task_name()
        tasks.add(user_task)
        self.interface.new_task_created()
        return tasks

    def update(self):
        self.list()
        task_index = None
        while task_index is None:
            try:
                task_index = self.interface.ask_nb_of_task_to_modify()
                if isinstance(int(task_index), int):
                    task_index = int(task_index) - 1
                else:
                    raise NotAnIntException()
            except NotAnIntException:
                self.interface.not_an_int_error()
            else:
                if task_index < 0 or task_index + 1 > len(tasks.list):
                    self.interface.task_does_not_exist()
                else:
                    new_task_name = self.interface.ask_new_task_name()
                    tasks.list[task_index] = tasks.list[task_index].update(new_task_name)
                    self.interface.modified_task_notification()
                return tasks

    def close(self):
        task_index = None
        while task_index is None:
            try:
                self.list()
                task_index = self.interface.ask_nb_of_task_to_close()
                if isinstance(int(task_index), int):
                    task_index = int(task_index) - 1
                else:
                    raise NotAnIntException()
            except NotAnIntException:
                self.interface.not_an_int_error()
            else:
                if task_index < 0 or task_index + 1 > len(tasks.list):
                    self.interface.task_does_not_exist()
                else:
                    tasks.list[task_index] = tasks.list[task_index].close()
                    self.interface.closed_task_notification()
                return tasks


if __name__ == '__main__':
    tasks = TasksList()
    app = Application()
    app.launch()
