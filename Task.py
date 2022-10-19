class Task:

    def __init__(self, name, status=False):
        self.name = name

    def update(self, new_name):
        self.name = new_name


