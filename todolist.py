class InterfaceDisplay:

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

    def add_task(self, interface_display):
        task_name = input("Saisir la tache : ")
        task = Task(task_name)
        interface_display.print(f'Vous venez de créer la tache: {task.name}')
        self.tasks_list.append(task)
        return self.tasks_list

    def update_task_in_list(self, interface_display):
        if not self.tasks_list:
            interface_display.print("Pas de tâche à afficher")
        else:
            index = len(self.tasks_list)
            while index >= len(self.tasks_list):
                try:
                    self.display_all_tasks(interface_display)
                    index = int(input("Saissez le numéro de la tâche à renommer (à partir de 0)"))
                    if index >= len(self.tasks_list) or index < 0:
                        raise InvalidValueException
                except InvalidValueException as e:
                    interface_display.print(e)
                except Exception:
                    interface_display.print("Merci de saisir un nombre")
            self.tasks_list[index] = self.tasks_list[index].update_task(interface_display)
        return self.tasks_list

    def mark_task_as_done_in_list(self, interface_display):
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
                    self.display_pending_tasks(interface_display)
                    index = int(input("Saissez le numéro de la tâche à clôturer (à partir de 0)"))
                    if index >= len(self.tasks_list) or index < 0:
                        raise InvalidValueException
                except InvalidValueException as e:
                    interface_display.print(e)
                except Exception:
                    interface_display.print("Merci de saisir un nombre")
            self.tasks_list[index].mark_task_as_done(interface_display)
        return self.tasks_list

    def display_pending_tasks(self, interface_display):
        interface_display.print("******* Toutes vos tâches en cours: *******")
        for task in self.tasks_list:
            if task.status == "A faire":
                interface_display.print(f"{task.name} => {task.status}")
        return self.tasks_list

    def display_all_tasks(self, interface_display):
        interface_display.print("******* Toutes vos tâches: *******")
        self.display_pending_tasks(interface_display)
        self.display_done_tasks(interface_display)
        return self.tasks_list

    def display_done_tasks(self, interface_display):
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

    def mark_task_as_done(self, interface_display):
        self.status = "Terminée"
        interface_display.print(f"Votre tâche {self.name} est marquée comme terminée")
        return self


class Menu:

    def __init__(self, tasks):
        self.menu_options = {
            "add": ("Ajouter une tâche", tasks.add_task),
            "update": ("Changer le nom d'une tâche", tasks.update_task_in_list),
            "done": ("Marquer une tâche comme terminée", tasks.mark_task_as_done_in_list),
            "list": ("Lister les tâches en cours", tasks.display_pending_tasks),
            "list_done": ("Lister les tâches terminées", tasks.display_done_tasks),
            "list_all": ("Lister toutes les tâches", tasks.display_all_tasks),
        }

    def do_action(self, command, interface_display):
        if command in self.menu_options.keys():
            return self.menu_options[command][1](interface_display)
        else:
            interface_display.print("Commande invalide")

    def display(self, interface_display):
        for key, value in self.menu_options.items():
            interface_display.print(key + " : " + value[0])


class App:

    def start(self):
        interface_display = InterfaceDisplay()
        tasks = TasksList()
        menu = Menu(tasks)
        menu.display(interface_display)
        command = input("\nMerci de saisir une commande : ")
        while command != "quit":
            tasks.tasks_list = menu.do_action(command, interface_display)
            command = input("\nMerci de saisir une commande : ")
        interface_display.print("Goodbye!")

    def do_action(self, command, tasks_list, menu, interface_display):
        try:
            if command in menu:
                tasks_list = menu[command][2](interface_display)
            else:
                raise InvalidCommandException
        except InvalidCommandException as e:
            interface_display.print(e)
        return tasks_list


if __name__ == "__main__":
    app = App()
    app.start()
