class Task:
    label = None
    is_done = False

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label

    def close(self):
        self.is_done = True
        return self

    def update(self, new_label):
        self.label = new_label
        return self
