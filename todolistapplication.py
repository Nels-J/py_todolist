class TodoListApplication:
    def __init__(self):
        self.tasks: list = []

    @staticmethod
    def print_menu():
        print("voici le menu :")
        print("Ajouter une tâche (commande 'add')")
        print("Effectuer une tâche (commande 'done')")
        print("Modifier le libellé d'une tâche (commande 'update')")
        print("Lister les tâches en cours (commande 'list')")
        print("Lister les tâches terminées (commande 'list-done')")
        print("Lister toutes les tâches (commande 'list-all')")
        print("Quitter (command 'quit')")

    def add(self):
        task_name = input("Quel est le nom de votre nouvelle tache ?")
        task_status = False
        self.tasks.append((task_name, task_status))

    def done(self):
        task_to_ckeck = input('Quelle tache souhaitez-vous accomplir ?')
        task_status = True
        self.tasks[int(task_to_ckeck) - 1] = (self.tasks[int(task_to_ckeck) - 1][0], task_status)

    def update(self):
        task_to_update = input('Quelle tâche voulez vous modifier ?')
        new_name = input('Quel est le nouveau nom de votre tâche ?')
        self.tasks[int(task_to_update) - 1] = (new_name, self.tasks[int(task_to_update) - 1][1])

    def list_in_progress(self):
        print('Liste des tâches en cours:')
        number_of_tasks_in_progress = 0
        for count, task in enumerate(self.tasks):
            if not task[1]:
                number_of_tasks_in_progress += 1
                print(count + 1, '-', task[0])
        if number_of_tasks_in_progress == 0:
            print('Aucune tâche en cours')

    def list_done(self):
        print('Liste des tâches terminées:')
        number_of_tasks_done = 0
        for count, task in enumerate(self.tasks):
            if task[1]:
                number_of_tasks_done += 1
                print(count + 1, '-', task[0])
        if number_of_tasks_done == 0:
            print('Aucune tâche terminée')

    def list_all(self):
        self.list_in_progress()
        self.list_done()

    def user_input(self, user_choice: str):
        choices = {
            'add': self.add,
            'done': self.done,
            'update': self.update,
            'list': self.list_in_progress,
            'list-done': self.list_done,
            'list-all': self.list_all,
        }
        try:
            choices[user_choice]()
        except Exception:
            print("Commande inexistante")
        return self.tasks

    def main(self):
        self.print_menu()
        user_choice = input('Que souhaitez-vous faire ?\n')
        while user_choice != "quit":
            self.tasks = self.user_input(user_choice)
            self.print_menu()
            user_choice = input('Que souhaitez-vous faire ?\n')


if __name__ == '__main__':
    test = TodoListApplication()
    test.main()
    print('╭∩╮(UwU)╭∩╮')
