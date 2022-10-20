from exceptions import NotInListIndexException, NotIntegerException, NotImplementedException, InvalidCommandException
from Task import Task


class TasksList:

    def __init__(self):
        self.list = []

    def add_task(self, list_tasks, interface):
        new_task_name = input('Name of task :')
        new_task = Task(new_task_name)
        self.list.append(new_task)
        interface.print('task saved ;-)')
        return self.list

    def close_task(self, list_tasks, interface):
        for i, name in enumerate(self.list):
            interface.print(f"tache n°: {i} {name[0]}")

        try:
            index_task_to_close = int(input('What task do you want to close?'))
            if index_task_to_close >= len(self.list):
                raise NotInListIndexException

            self.list[index_task_to_close] = (self.list[index_task_to_close][0], True)
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

        for i, name in enumerate(self.list):
            interface.print(f"tache n°: {i} {name[0]}")
        try:
            index_task_to_update = int(input('What task do you want to update?'))
            if index_task_to_update >= len(self.list):
                raise NotInListIndexException
            new_task_name = input('What is new name of the task?')
            self.list[index_task_to_update] = (new_task_name, self.list[index_task_to_update][1])
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
        interface.print("List of your pending tasks :")
        for task in self.list:
            if not task.status:
                interface.print(task.name)

    def list_done_tasks(self, list_tasks, interface):
        interface.print("List of your tasks already done :")
        for count, task in enumerate(self.list):
            if task.status:
                interface.print(str(count) + " - " + task.name)

    def list_all_tasks(self, list_tasks, interface):
        try:
            if len(self.list) == 0:
                interface.print('No tasks')
                return
            self.list_pending_tasks(self.list, interface)
            self.list_done_tasks(self.list, interface)
        except Exception as e:
            print(e)
