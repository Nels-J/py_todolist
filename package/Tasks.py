from package.Task import Task


class Tasks:
    def __init__(self):

        self.file = open("persistance.txt", "w+")

    def add(self, label):
        task_label = Task(label)
        self.file.write(f'{task.get_task()}\n')
        print(self.file.read())

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

    def close_file(self):
        self.file.close()
