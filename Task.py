class Task:

    def __init__(self, name, status=False):
        self.name = name
        self.status = status

    def update(self, new_name):
        self.name = new_name

    def done(self):
        self.status = True


