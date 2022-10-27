class Task:

    label = None
    is_done = False

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label



