from exception import InvalidValueException


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
            self.tasks_list[index] = self.tasks_list[index].mark_task_as_done(interface_display)
        return self.tasks_list

    def display_pending_tasks(self, interface_display):
        interface_display.print("******* Toutes vos tâches en cours: *******")
        for index, task in enumerate(self.tasks_list):
            if task.status == "A faire":
                interface_display.print(f"{index} : {task.name}")
        return self.tasks_list

    def display_done_tasks(self, interface_display):
        interface_display.print("******* Toutes vos tâches terminées: *******")
        for index, task in enumerate(self.tasks_list):
            if task.status == "Terminée":
                interface_display.print(f"{index} : {task.name}")
        return self.tasks_list

    def display_all_tasks(self, interface_display):
        interface_display.print("******* Toutes vos tâches: *******")
        self.display_pending_tasks(interface_display)
        self.display_done_tasks(interface_display)
        return self.tasks_list


class Task:
    def __init__(self, name):
        self.name = name
        self.status = "A faire"
        fichier = open("tasks.txt", 'a')
        fichier.write("[ ] " + name + "\n")
        fichier.close()

    def update_task(self, interface_display):
        self.name = input("Veuillez renommer votre tâche")
        interface_display.print(f"Votre tâche est renommée en : {self.name}")
        return self

    def mark_task_as_done(self, interface_display):
        self.status = "Terminée"
        interface_display.print(f"Votre tâche {self.name} est marquée comme terminée")
        return self
