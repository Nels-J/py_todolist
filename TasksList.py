from Task import Task


class TasksList:
    list_tasks = []

    def add(self, label):
        task = Task(label)
        self.list_tasks.append(task)

    def list_according_to_status(self, status):
        tasks = []
        for index, item in enumerate(self.list_tasks):
            if item.is_done == status:
                tasks.append((index, item))
        return tasks
