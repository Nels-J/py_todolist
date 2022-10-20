class Task:

    def __init__(self, name):
        self.name = name
        self.status = False

    def update(self, new_name):
        self.name = new_name