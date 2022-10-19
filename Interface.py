class Interface:

    def print_menu(self):
        self.print("add       : add new task")
        self.print("done      : close task")
        self.print("update    : amend task name")
        self.print("list      : list pending tasks")
        self.print("list-done : list closed tasks")
        self.print("list-all  : list all tasks")
        self.print("quit      : exit the application")

    def input(self, message):
        return input(message)

    def print(self, message):
        print(message)
