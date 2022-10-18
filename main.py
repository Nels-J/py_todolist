def add():
    user_task = input("Veuillez saisir votre nouvelle tâche")
    return user_task

    # print('VOUS AVEZ TAPE ADD')
    # raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def done():
    print('VOUS AVEZ TAPE DONE')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def update():
    print('VOUS AVEZ TAPE UPDATE')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def list(task):
    print(task)

    # print('VOUS AVEZ TAPE LIST')
    # raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def list_done():
    print('VOUS AVEZ TAPE LIST DONE')
    raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def list_all():
    print('VOUS AVEZ TAPE LIST ALL')
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


def user_input(user_choice, task):
    try:
        if user_choice == 'add':
            return add()
        elif user_choice == 'done':
            done()
        elif user_choice == 'update':
            update()
        elif user_choice == 'list':
            return list(task)
        elif user_choice == 'list-done':
            list_done()
        elif user_choice == 'list-all':
            list_all()
        else:
            raise ValueError('La fonctionnalité n\'existe pas !')

    except ValueError as e:
        print(e)


def main():
    want_to_quit = False
    task = ""
    while not want_to_quit:
        print_menu()
        user_choice = input('Que souhaitez-vous faire ?\n')
        if user_choice == 'quit':
            want_to_quit = True
        else:
            task = user_input(user_choice, task)


if __name__ == '__main__':
    main()
