class InterfaceDisplay:

    def display_menu(self):
        print("Ajouter une ligne : add ")
        print("Marquer comme terminée : done")
        print("Mettre à jour : update")
        print("Afficher la liste des tâches non terminées: list")
        print("Afficher la liste des tâches terminées : list_done")
        print("Afficher toutes les tâches : all")
        print("Quitter : quit")

    def print(self, message):
        print(message)


class InvalidCommandException(Exception):
    def __init__(self):
        super().__init__("Commande invalide")


class InvalidValueException(Exception):
    def __init__(self):
        super().__init__("Valeur invalide")


class TasksList:

    def __init__(self):
        self.tasks_list = []

    def add_task(self, tasks, interface_display):
        task = (input("Saisir la tache : "), "A faire")
        interface_display.print(f'Vous venez de créer la tache: {task[0]}')
        self.tasks_list.append(task)
        interface_display.print(f"tasks=> {self.tasks_list}")
        return self.tasks_list

def main():
    interface_display = InterfaceDisplay()
    tasks = TasksList()
    menu = {
        "add": ("Ajouter une tâche", "add", tasks.add_task),
        "update": ("Changer le nom d'une tâche", "update", update),
        "done": ("Marquer une tâche comme terminée", "done", done),
        "list": ("Lister les tâches en cours", "list", display_list),
        "list_done": ("Lister les tâches terminées", "list_done", list_done),
        "list_all": ("Lister toutes les tâches", "list_all", list_all),
    }


    interface_display.display_menu()
    command = input("\nEnter a command: ")
    while command != "quit":
        tasks.tasks_list = do_action(command, tasks.tasks_list, menu, interface_display)
        command = input("\nEnter a command: ")
    interface_display.print("Goodbye!")


def done(tasks, interface_display):
    pending = []
    for task in tasks:
        if task[1] == "A faire":
            pending.append(task)
    if not pending:
        interface_display.no_tasks()
    else:
        index = len(tasks)
        while index >= len(tasks):
            try:
                index = int(input("Saissez le numéro de la tâche à clôturer (à partir de 0)"))
                if index >= len(tasks):
                    raise InvalidValueException
            except InvalidValueException as e:
                interface_display.print(e)
        tasks[index] = tasks[index][0], "Terminée"
        interface_display.print(f'Votre tâche: {tasks[index][0]} est à présent: {tasks[index][1]}')
        list_all(tasks, interface_display)
    return tasks

def update(tasks, interface_display):
    if not tasks:
        interface_display.print("Pas de tâche à afficher")
    else:
        index = len(tasks)
        while index >= len(tasks):
            try:
                index = int(input("Saissez le numéro de la tâche à renommer (à partir de 0)"))
                if index >= len(tasks):
                    raise InvalidValueException
            except InvalidValueException as e:
                interface_display.print(e)
        tasks[index] = input("Veuillez renommer votre tâche"), tasks[index][1]
        interface_display.print(f"Votre tâche est renommée en : {tasks[index][0]}")
        list_all(tasks, interface_display)
    return tasks


def display_list(tasks, interface_display):
    interface_display.print("******* Toutes vos tâches en cours: *******")
    for task in tasks:
        if task[1] == "A faire":
            interface_display.print(f"{task[0]} => {task[1]}")
    return tasks


def list_all(tasks, interface_display):
    interface_display.print("******* Toutes vos tâches: *******")
    display_list(tasks, interface_display)
    list_done(tasks, interface_display)
    return tasks


def list_done(tasks, interface_display):
    interface_display.print("******* Toutes vos tâches terminées: *******")
    for task in tasks:
        if task[1] == "Terminée":
            interface_display.print(f"{task[0]} => {task[1]}")
    return tasks


def do_action(command, tasks, menu, interface_display):
    try:
        if command in menu:
            tasks = menu[command][2](tasks, interface_display)
        else:
            raise InvalidCommandException
    except InvalidCommandException as e:
        interface_display.print(e)
    return tasks


if __name__ == "__main__":
    main()
