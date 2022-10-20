from task import Task


class ListTasks:

    def __init__(self):
        self.tasks: list = []

    def addTask(self, task_name, task_status):
        task = Task(task_name, task_status)
        self.tasks.append(task)

    def update_task(self, task_to_update, new_name):
        if len(self.tasks) > int(task_to_update) - 1 > 0:
            self.tasks[int(task_to_update)-1].name = new_name
        else:
            raise Exception("La tache n'existe pas !")

    def done_task(self, task_to_check, task_status):
        if len(self.tasks) > int(task_to_check)-1 > 0:
            self.tasks[int(task_to_check)-1].status = task_status
        else:
            raise Exception("La tache n'existe pas !")
