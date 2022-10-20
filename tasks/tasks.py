from tasks.task import Task


class Tasks:
    list = []

    def add(self, label):
        task = Task(label)
        self.list.append(task)

    def list_wanted_tasks(self, wanted_status):
        wanted_tasks = []
        for index, task in enumerate(self.list):
            if task.status == wanted_status:
                wanted_tasks.append((index, task.label))
        return wanted_tasks

    def list_pending(self):
        return self.list_wanted_tasks(False)

    def list_done(self):
        return self.list_wanted_tasks(True)
