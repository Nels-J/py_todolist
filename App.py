class Application:
    def __init__(self):
        self.display_menu()
        self.input = input()
        self.task_list = []
        self.choice = {
            "add": self.add,
            "done": self.done,
            "update": self.update,
            "list": self.list_all,
            "list not done": self.list_not_done,
            "list done": self.list_done,
        }

    def run(self):
        self.display_menu()
        user_input = input()
        while user_input != "quit":
            try:
                self.display_menu()
                if user_input in self.choice:
                    self.choice[user_input]()
            except Exception as e:
                self.exceptions(e)
        self.display_menu()

    def add(self, task):
        return self.task_list.append(task)

    def done(self):
        pass

    def update(self):
        pass

    def list_all(self):
        for task in self.task_list:
            print(task)

    def list_not_done(self):
        pass

    def list_done(self):
        pass

    def exceptions(self, e):
        print(e)

    def display_menu(self):
        print("""
            \nAjouter une tâche (add)
            \nEffectuer une tâche (done)
            \nModifier le libellé d'une tâche (update)
            \nLister les tâches en cours (list)
            \nLister les tâches terminées (list-done)
            \nLister toutes les tâches (list-all)"
            \nQuitter (quit)")
            \n********Que voulez-vous faire ?**********
        """)


if __name__ == "__main__":
    app = Application()
    app.run()

