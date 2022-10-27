from Task import Task


class TasksList:
    list_tasks = []

    def add(self, label):
        task = Task(label)
        self.list_tasks.append(task)

