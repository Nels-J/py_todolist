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
                "done": ("Effectuer une tâche", self.done),
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
                raise ValueError('La fonctionnalité n\'existe pas !')
        except ValueError as e:
            print(e)
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
            print("Les tâches en cours sont :")
            for pending_task in pending_tasks:
                print(pending_task[0] + 1, ":", pending_task[1].label)
        else:
            self.interface.no_current_undone_task()

    def list_done(self, tasks):
        done_tasks = tasks.list_according_to_status(True)
        if len(done_tasks) > 0:
            print("Les tâches terminées sont :")
            for done_task in done_tasks:
                print(done_task[0] + 1, ":", done_task[1].label)
        else:
            self.interface.no_current_done_task()

    def list_all(self, tasks):
        done_tasks = []
        pending_tasks = []
        for index, task in enumerate(tasks.list_tasks):
            if task.is_done:
                done_tasks.append((task, index))
            else:
                pending_tasks.append((task, index))
        if len(pending_tasks) > 0:
            print('Voici les tâches en cours :')
            for task in pending_tasks:
                print(task[1] + 1, ":", task[0].label)
        if len(done_tasks) > 0:
            print('Voici les tâches terminées :')
            for task in done_tasks:
                print(task[1] + 1, ":", task[0].label)

    def add(self, tasks):
        user_task = input("Veuillez saisir votre nouvelle tâche: ")
        tasks.add(user_task)
        print("Tâche créée")
        return tasks

    def update(self, tasks):
        self.list(tasks)
        index_tache = None
        while index_tache is None:
            try:
                index_tache = int(input("Indiquez le numéro de la tâche à modifier")) - 1
            except Exception as err:
                print("Entrée invalide : merci d'entrer un entier")
        if index_tache < 0 or index_tache + 1 > len(tasks.list_tasks):
            print("Cette tâche n'existe pas")
        else:
            nouveau_nom_tache = input("Veuillez saisir le nouveau nom de la tâche")
            tasks.list_tasks[index_tache] = tasks.list_tasks[index_tache].update(nouveau_nom_tache)
            print("Tâche modifée")
        return tasks

    def done(self, tasks):
        index_tache = None
        while index_tache is None:
            try:
                self.list(tasks)
                index_tache = int(input("Indiquez le numéro de la tâche terminée : ")) - 1
            except Exception as err:
                print("Entrée invalide : merci d'entrer un entier")
        if index_tache < 0 or index_tache + 1 > len(tasks.list_tasks):
            print("Cette tâche n'existe pas")
        else:
            tasks.list_tasks[index_tache] = tasks.list_tasks[index_tache].close()
        return tasks


if __name__ == '__main__':
    app = Application()
    app.launch()
