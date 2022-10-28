import os

from exceptions import NotInListIndexException, NotIntegerException, NotImplementedException, InvalidCommandException
from Task import Task
import pickle


class TasksList:

    def __init__(self):
        self.list = []

    def get_binary_file(self):
        with open('databinairy.txt', 'rb') as file:
            if os.path.getsize('databinairy.txt') > 0:
                return pickle.load(file)

    def write_binary_file(self, param):
        fichier = open("databinairy.txt", "wb")
        pickle.dump(param, fichier)
        fichier.close()

    def getfile(self):
        fichier = open("data.txt", "r")
        print(fichier.read().splitlines())
        fichier.close()

    def writefile(self, param):
        fichier = open("data.txt", "w")
        for item in param:
            fichier.write(item.name + " => " + str(item.status) + "\n")
        fichier.close()

    def add_task(self, list_tasks, interface):
        new_task_name = input('Name of task :')
        new_task = Task(new_task_name)
        self.list.append(new_task)
        self.writefile(self.list)
        interface.print('task saved ;-)')
        return self.list

    def close_task(self, list_tasks, interface):
        for i, task in enumerate(self.list):
            interface.print(f"tache n°: {i} {task.name}")

        try:
            index_task_to_close = int(input('What task do you want to close?'))
            if index_task_to_close >= len(self.list):
                raise NotInListIndexException

            self.list[index_task_to_close].done()
            self.writefile(self.list)
            self.write_binary_file(self.list)
            interface.print('Task closed')

        except ValueError:
            try:
                raise NotIntegerException
            except NotIntegerException:
                interface.print("not integer exception")
                self.close_task(self.list, interface)
        except NotInListIndexException:
            interface.print("l'index n'est pas valide")
            self.close_task(self.list, interface)

    def update_task(self, list_task, interface):
        if len(self.list) == 0:
            interface.print('No tasks')
            return

        for i, task in enumerate(self.list):
            interface.print(f"tache n°: {i} {task.name}")
        try:
            index_task_to_update = int(input('What task do you want to update?'))
            if index_task_to_update >= len(self.list):
                raise NotInListIndexException
            new_task_name = input('What is new name of the task?')
            self.list[index_task_to_update].update(new_task_name)
            self.writefile(self.list)
            self.write_binary_file(self.list)
            interface.print('Task name update')
        except ValueError:
            try:
                raise NotIntegerException
            except NotIntegerException:
                interface.print("not integer exception")
                self.update_task(self.list, interface)
        except NotInListIndexException:
            interface.print("l'index n'est pas valide")
            self.update_task(self.list, interface)

    def list_pending_tasks(self, list_tasks, interface):
        # print(f"list_pending_tasks => {self.list}")
        interface.print("List of your pending tasks :")
        for count, task in enumerate(self.list):
            if not task.status:
                interface.print(f"{count}) {task.name} => {task.status}")

    def list_done_tasks(self, list_tasks, interface):
        # print("list_done_tasks => {self.list}")
        interface.print("List of your tasks already done :")
        for count, task in enumerate(self.list):
            if task.status:
                interface.print(f"{count}) {task.name} => {task.status}")

    def list_all_tasks(self, list_tasks, interface):
        self.getfile()
        self.get_binary_file()
        # print("list_all_tasks => {self.list}")
        try:
            if len(self.list) == 0:
                interface.print('No tasks')
                return
            self.list_pending_tasks(self.list, interface)
            self.list_done_tasks(self.list, interface)
        except Exception as e:
            print(e)
