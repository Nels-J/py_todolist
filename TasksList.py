from Task import Task


class TasksList:
    list_tasks = []

    def add(self, label):
        task = Task(label)
        self.list_tasks.append(task)

    def list_according_to_status(self, status):
        tasks = []
        for index, task in enumerate(self.list_tasks):
            if task.is_done == status:
                tasks.append((index, task))
        return tasks
