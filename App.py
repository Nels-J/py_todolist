class Application:
    def __init__(self):
        self.status = True
        self.task = ""
        self.task_list = []
        self.choice = {
            "add": self.add,
            "done": self.done,
            "update": self.update,
            "list": self.list_all,
            "list not done": self.list_not_done,
            "list done": self.list_done,
            "menu": self.display_menu,
        }

    def run(self):
        self.display_menu()
        user_input = input("Please enter your command :")
        while user_input != "quit":
            try:
                if user_input in self.choice:
                    self.choice[user_input]()
                else:
                    raise NotImplementedError
            except Exception as e:
                self.exceptions(e)
            user_input = input("Please enter your command :")

    def add(self):
        self.task = input("What task should I add ?")
        return self.task_list.append((self.task, self.status))

    def done(self):
        self.list_not_done()
        user_input = int(input("Quelle tache voulez vous effectuer ?")) - 1
        self.task_list[user_input] = self.task_list[user_input][0], False

    def update(self):
        self.list_all()
        user_input = int(input("Quelle tache voulez vous editer ?")) - 1
        user_new_task = input("Donner un nouveau libellé: ")
        self.task_list[user_input] = (user_new_task, self.task_list[user_input][self.status])

    def list_all(self):
        if len(self.task_list) == 0:
            print("il n'y a rien ici")
        else:
            print("En cours")
            self.list_not_done()
            print("Terminée")
            self.list_done()

    def list_not_done(self):
        for idx, item in enumerate(self.task_list):
            if item[1]:
                print(f"{idx + 1},   correspond à la tache  ,  {item[0]}")

    def list_done(self):
        for idx, item in enumerate(self.task_list):
            if not item[1]:
                print(f"{idx + 1},   correspond à la tache  ,  {item[0]}")

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
            \nafficher le menu (menu)")
            \n********Que voulez-vous faire ?**********
        """)


if __name__ == "__main__":
    app = Application()
    app.run()

