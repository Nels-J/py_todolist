from Exceptions import MenuEntryDoesNotExist, NotAnIntException
from Interface import Interface
from Task import Task
from TasksList import TasksList

class Application:
    def __init__(self):
        self.interface = Interface()
        pass

    def launch(self):
        want_to_quit = False
        tasks = TasksList()
        menu = {"add": ("Ajouter une tâche", self.add),
                "close": ("Terminer une tâche", self.close),
                "update": ("Modifier le libellé d'une tâche", self.update),
                "list": ("Lister les tâches en cours", self.list),
                "list-done": ("Lister les tâches terminées", self.list_done),
                "list-all": ("Lister toutes les tâches", self.list_all),
                "test": ("test", self.scenario)
                }
        self.interface.print_menu(menu)
        while not want_to_quit:
            user_choice = self.interface.ask_action()
            if user_choice == 'quit':
                want_to_quit = True
            else:
                tasks = self.user_command(tasks, user_choice, menu)

    def is_valid(self, user_choice, menu):
        if user_choice in menu:
            return True
        else:
            return False

    def user_command(self, tasks, user_choice, menu):
        try:
            if self.is_valid(user_choice, menu):
                menu[user_choice][1](tasks)
            else:
                raise MenuEntryDoesNotExist()
        except MenuEntryDoesNotExist:
            self.interface.menu_entry_does_not_exist()
        return tasks

    def scenario(self, tasks):
        tasks.add(Task('t1'))
        tasks.add(Task('T2'))
        # self.update_task(tasks, 1, "new T2")
        # self.close_task(tasks, 1)
        self.list_all(tasks)

    def list(self, tasks):
        pending_tasks = tasks.list_according_to_status(False)
        if len(pending_tasks) > 0:
            self.interface.undone_tasks_are()
            for pending_task in pending_tasks:
                self.interface.display_task_with_nb(pending_task)
        else:
            self.interface.no_undone_task()

    def list_done(self, tasks):
        done_tasks = tasks.list_according_to_status(True)
        if len(done_tasks) > 0:
            self.interface.done_tasks_are()
            for done_task in done_tasks:
                self.interface.display_task_with_nb(done_task)
        else:
            self.interface.no_done_task()

    def list_all(self, tasks):
        self.list(tasks)
        self.list_done(tasks)

    def add(self, tasks):
        user_task = self.interface.ask_new_task_name()
        tasks.add(user_task)
        self.interface.new_task_created()
        return tasks

    def update(self, tasks):
        self.list(tasks)
        index_tache = None
        while index_tache is None:
            try:
                index_tache = self.interface.ask_nb_of_task_to_modify()
                if isinstance(index_tache, int):
                    index_tache = int(index_tache) - 1
                else:
                    raise NotAnIntException()
            except NotAnIntException:
                self.interface.not_an_int_error()
            else:
                if index_tache < 0 or index_tache + 1 > len(tasks.list_tasks):
                    self.interface.task_does_not_exist()
                else:
                    nouveau_nom_tache = self.interface.ask_new_task_name()
                    tasks.list_tasks[index_tache] = tasks.list_tasks[index_tache].update(nouveau_nom_tache)
                    self.interface.modified_task_notification()
                return tasks

    def close(self, tasks):
        index_tache = None
        while index_tache is None:
            try:
                self.list(tasks)
                index_tache = self.interface.ask_nb_of_task_to_close()
                if isinstance(index_tache, int):
                    index_tache = int(index_tache) - 1
                else:
                    raise NotAnIntException()
            except NotAnIntException:
                self.interface.not_an_int_error()
            else:
                if index_tache < 0 or index_tache + 1 > len(tasks.list_tasks):
                    self.interface.task_does_not_exist()
                else:
                    tasks.list_tasks[index_tache] = tasks.list_tasks[index_tache].close()
                    self.interface.closed_task_notification()
                return tasks


if __name__ == '__main__':
    app = Application()
    app.launch()
