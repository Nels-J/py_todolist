from Task import Task


class TasksList:
    list_tasks = []

    def add(self, label):
        task = Task(label)
        self.list_tasks.append(task)


class Application:
    def __init__(self):
        pass

    def launch(self):
        want_to_quit = False
        tasks = TasksList()
        menu = {"add": ("Ajouter une tâche", self.add),
                "done": ("Effectuer une tâche", done),
                "update": ("Modifier le libellé d'une tâche", self.update),
                "list": ("Lister les tâches en cours", self.list),
                "list-done": ("Lister les tâches terminées", list_done),
                "list-all": ("Lister toutes les tâches", self.list_all),
                "test": ("test", self.scenario)
                }
        print_menu(menu)
        while not want_to_quit:
            user_choice = input('Que souhaitez-vous faire ?\n')
            if user_choice == 'quit':
                want_to_quit = True
            else:
                tasks = user_command(tasks, user_choice, menu)

    def add(self, tasks):
        user_task = input("Veuillez saisir votre nouvelle tâche: ")
        task = Task(user_task)
        tasks.list_tasks.append(task)
        print("Tâche créée")
        return tasks

    def list(self, tasks):
        pending_tasks = []
        for index, item in enumerate(tasks.list_tasks):
            if not item.is_done:
                pending_tasks.append((index, item))
        if len(pending_tasks) > 0:
            print("Les tâches en cours sont :")
            for pending_task in pending_tasks:
                print(pending_task[0] + 1, ":", pending_task[1].label)
        else:
            print("Aucune tâche en cours pour l'instant!")

    def list_done(self, tasks):
        done_tasks = []
        for index, item in enumerate(tasks.list_tasks):
            if item.is_done:
                done_tasks.append((index, item))
        if len(done_tasks) > 0:
            print("Les tâches terminées sont :")
            for done_task in done_tasks:
                print(done_task[0] + 1, ":", done_task[1].label)
        else:
            print("Aucune tâche finie pour l'instant!")

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

    def scenario(self, tasks):
        tasks.add(Task('t1'))
        tasks.add(Task('T2'))
        self.update_task(tasks, 1, "new T2")
        close_task(tasks, 1)
        self.list_all(tasks)

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
            self.update_task(tasks, index_tache, nouveau_nom_tache)
            print("Tâche modifée")
        return tasks

    def update_task(self, tasks, task_number, new_name):
        tasks.list_tasks[task_number].label = new_name
        return tasks


def done(tasks):
    index_tache = None
    while index_tache is None:
        try:
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
            index_tache = int(input("Indiquez le numéro de la tâche terminée : ")) - 1
        except Exception as err:
            print("Entrée invalide : merci d'entrer un entier")
    if index_tache < 0 or index_tache + 1 > len(tasks.list_tasks):
        print("Cette tâche n'existe pas")
    else:
        tasks = close_task(tasks, index_tache)
    return tasks


def list_done(tasks):
    done_tasks = []
    for index, item in enumerate(tasks.list_tasks):
        if item.is_done:
            done_tasks.append((index, item))
    if len(done_tasks) > 0:
        print("Les tâches terminées sont :")
        for done_task in done_tasks:
            print(done_task[0] + 1, ":", done_task[1].label)
    else:
        print("Aucune tâche finie pour l'instant!")


def print_menu(menu):
    print("Voici le menu :")
    for cle, valeur in menu.items():
        print(cle, ":", valeur[0])
    print("quit : Quitter")


def is_valid(user_choice, menu):
    if user_choice in menu:
        return True
    else:
        return False


def user_command(tasks, user_choice, menu):
    try:
        if is_valid(user_choice, menu):
            menu[user_choice][1](tasks)
        else:
            raise ValueError('La fonctionnalité n\'existe pas !')
    except ValueError as e:
        print(e)
    return tasks


def close_task(tasks, task_number):
    tasks.list_tasks[task_number].is_done = True
    return tasks





if __name__ == '__main__':
    app = Application()
    app.launch()
