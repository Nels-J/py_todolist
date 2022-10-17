def add():
    print('VOUS AVEZ TAPE ADD')


def quit_menu():
    print('Vous avez quitté la to do list.')


def print_menu():
    print("voici le menu :")
    print("Ajouter une tâche (commande 'add')")
    print("Effectuer une tâche (commande 'done')")
    print("Modifier le libellé d'une tâche (commande 'update')")
    print("Lister les tâches en cours (commande 'list')")
    print("Lister les tâches terminées (commande 'list-done')")
    print("Lister toutes les tâches (commande 'list-all')")
    print("Quitter (command 'quit')")


def user_input():
    user_choice = input('Que souhaitez-vous faire ?\n')
    try:
        if user_choice == 'add':
            add()
        else:
            raise ValueError

    except ValueError:
        print('La fonctionnalité n\'a pas encore été implémentée !')


if __name__ == '__main__':
    want_to_quit = False
    while not want_to_quit:
        print_menu()
        user_input()
