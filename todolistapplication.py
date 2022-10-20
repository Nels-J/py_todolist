from actionMenu import ActionMenu


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

    def start(self):
        menu = ActionMenu()
        self.print_menu()
        user_choice = input('Que souhaitez-vous faire ?\n')
        while user_choice != "quit":
            self.tasks = menu.user_input(user_choice)
            self.print_menu()
            user_choice = input('Que souhaitez-vous faire ?\n')


if __name__ == '__main__':
    test = TodoListApplication()
    test.start()
    print('╭∩╮(UwU)╭∩╮')
