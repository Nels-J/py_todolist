from UI import UI


class Task:
    label = None
    status = False

    def __init__(self, label):
        self.label = label

    def done(self):
        self.status = True

    def update(self, task_new_name):
        self.label = task_new_name
