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
        task_name = input("Saisir la tache : ")
        task = Task(task_name)
        interface_display.print(f'Vous venez de créer la tache: {task.name}')
        self.tasks_list.append(task)
        self.display_all_tasks(self.tasks_list, interface_display)
        return self.tasks_list

    def update_task_in_list(self, tasks, interface_display):
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
            self.tasks_list[index] = self.tasks_list[index].update_task(interface_display)
            self.display_all_tasks(self.tasks_list, interface_display)
        return self.tasks_list

    def mark_task_as_done(self, tasks, interface_display):
        pending_tasks = []
        for task in self.tasks_list:
            if task.status == "A faire":
                pending_tasks.append(task)
        if not pending_tasks:
            interface_display.print("Il n'y a pas de tâche en cours")
        else:
            index = len(self.tasks_list)
            while index >= len(self.tasks_list):
                try:
                    index = int(input("Saissez le numéro de la tâche à clôturer (à partir de 0)"))
                    if index >= len(self.tasks_list):
                        raise InvalidValueException
                except Exception:
                    interface_display.print("Merci de saisir un nombre")
                except InvalidValueException as e:
                    interface_display.print(e)
            self.tasks_list[index].status = "Terminée"
            interface_display.print(
                f'Votre tâche: {self.tasks_list[index].name} est à présent: {self.tasks_list[index].status}')
            self.display_all_tasks(self.tasks_list, interface_display)
        return self.tasks_list

    def display_pending_tasks(self, tasks, interface_display):
        interface_display.print("******* Toutes vos tâches en cours: *******")
        for task in self.tasks_list:
            if task.status == "A faire":
                interface_display.print(f"{task.name} => {task.status}")
        return self.tasks_list

    def display_all_tasks(self, tasks, interface_display):
        interface_display.print("******* Toutes vos tâches: *******")
        self.display_pending_tasks(self.tasks_list, interface_display)
        self.display_done_tasks(self.tasks_list, interface_display)
        return self.tasks_list

    def display_done_tasks(self, tasks, interface_display):
        interface_display.print("******* Toutes vos tâches terminées: *******")
        for task in self.tasks_list:
            if task.status == "Terminée":
                interface_display.print(f"{task.name} => {task.status}")
        return self.tasks_list


class Task:
    def __init__(self, name):
        self.name = name
        self.status = "A faire"

    def update_task(self, interface_display):
        self.name = input("Veuillez renommer votre tâche")
        interface_display.print(f"Votre tâche est renommée en : {self.name}")
        return self


def main():
    interface_display = InterfaceDisplay()
    tasks = TasksList()
    menu = {
        "add": ("Ajouter une tâche", "add", tasks.add_task),
        "update": ("Changer le nom d'une tâche", "update", tasks.update_task_in_list),
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
