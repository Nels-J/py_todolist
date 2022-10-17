def add():
    print('VOUS AVEZ TAPE ADD')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def done():
    print('VOUS AVEZ TAPE DONE')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def update():
    print('VOUS AVEZ TAPE UPDATE')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def list():
    print('VOUS AVEZ TAPE LIST')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def list_done():
    print('VOUS AVEZ TAPE LIST DONE')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def list_all():
    print('VOUS AVEZ TAPE LIST ALL')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def quit_menu():
    print('Vous avez quitté la to do list.')
    print('VOUS AVEZ TAPE QUIT')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


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
        elif user_choice == 'quit':
            quit_menu()

        else:
            raise ValueError('La fonctionnalité n\'existe pas !')

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    want_to_quit = False
    while not want_to_quit:
        print_menu()
        user_input()
