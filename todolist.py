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

    def update_task(self, tasks, interface_display):
        if not self.tasks_list:
            interface_display.print("Pas de tâche à afficher")
        else:
            index = len(self.tasks_list)
            while index >= len(self.tasks_list):
                try:
                    index = int(input("Saissez le numéro de la tâche à renommer (à partir de 0)"))
                    if index >= len(self.tasks_list):
                        raise InvalidValueException
                except InvalidValueException as e:
                    interface_display.print(e)
            self.tasks_list[index] = input("Veuillez renommer votre tâche"), self.tasks_list[index][1]
            interface_display.print(f"Votre tâche est renommée en : {self.tasks_list[index][0]}")
            self.display_all_tasks(self.tasks_list, interface_display)
        return self.tasks_list

    def mark_task_as_done(self, tasks, interface_display):
        pending = []
        for task in self.tasks_list:
            if task[1] == "A faire":
                pending.append(task)
        if not pending:
            interface_display.no_tasks()
        else:
            index = len(self.tasks_list)
            while index >= len(self.tasks_list):
                try:
                    index = int(input("Saissez le numéro de la tâche à clôturer (à partir de 0)"))
                    if index >= len(self.tasks_list):
                        raise InvalidValueException
                except InvalidValueException as e:
                    interface_display.print(e)
            self.tasks_list[index] = self.tasks_list[index][0], "Terminée"
            interface_display.print(
                f'Votre tâche: {self.tasks_list[index][0]} est à présent: {self.tasks_list[index][1]}')
            self.display_all_tasks(self.tasks_list, interface_display)
        return self.tasks_list

    def display_pending_tasks(self, tasks, interface_display):
        interface_display.print("******* Toutes vos tâches en cours: *******")
        for task in self.tasks_list:
            if task[1] == "A faire":
                interface_display.print(f"{task[0]} => {task[1]}")
        return self.tasks_list

    def display_all_tasks(self, tasks, interface_display):
        interface_display.print("******* Toutes vos tâches: *******")
        self.display_pending_tasks(self.tasks_list, interface_display)
        self.display_done_tasks(self.tasks_list, interface_display)
        return self.tasks_list

    def display_done_tasks(self, tasks, interface_display):
        interface_display.print("******* Toutes vos tâches terminées: *******")
        for task in self.tasks_list:
            if task[1] == "Terminée":
                interface_display.print(f"{task[0]} => {task[1]}")
        return self.tasks_list


def main():
    interface_display = InterfaceDisplay()
    tasks = TasksList()
    menu = {
        "add": ("Ajouter une tâche", "add", tasks.add_task),
        "update": ("Changer le nom d'une tâche", "update", tasks.update_task),
        "done": ("Marquer une tâche comme terminée", "done", tasks.mark_task_as_done),
        "list": ("Lister les tâches en cours", "list", tasks.display_pending_tasks),
        "list_done": ("Lister les tâches terminées", "list_done", tasks.display_done_tasks),
        "list_all": ("Lister toutes les tâches", "list_all", tasks.display_all_tasks),
    }

    interface_display.display_menu()
    command = input("\nEnter a command: ")
    while command != "quit":
        tasks.tasks_list = do_action(command, tasks.tasks_list, menu, interface_display)
        command = input("\nEnter a command: ")
    interface_display.print("Goodbye!")


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
