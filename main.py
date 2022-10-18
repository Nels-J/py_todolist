def add():
    user_task = input("Veuillez saisir votre nouvelle tâche")
    task = (user_task, False)
    return task

    # print('VOUS AVEZ TAPE ADD')
    # raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def done(task):
    return task[0], True


def update(task):
    task_new_name = input("Veuillez saisir le nouveau nom de la tâche")
    done = task[1]
    return task_new_name, done


def list(task):
    print(task)


# print('VOUS AVEZ TAPE LIST')
# raise ValueError('La fonctionnalité n\'a pas encore été implémentée !')


def list_done(task):
    print(task)


def list_all(task):
    print(task)


def print_menu():
    print("voici le menu :")
    print("Ajouter une tâche (commande 'add')")
    print("Effectuer une tâche (commande 'done')")
    print("Modifier le libellé d'une tâche (commande 'update')")
    print("Lister les tâches en cours (commande 'list')")
    print("Lister les tâches terminées (commande 'list-done')")
    print("Lister toutes les tâches (commande 'list-all')")
    print("Quitter (command 'quit')")


def user_command(user_choice, task):
    try:
        if user_choice == 'add':
            return add()
        elif user_choice == 'done':
            return done(task)
        elif user_choice == 'update':
            return update(task)
        elif user_choice == 'list':
            list(task)
            return task
        elif user_choice == 'list-done':
            list_done(task)
        elif user_choice == 'list-all':
            list_all(task)
        else:
            raise ValueError('La fonctionnalité n\'existe pas !')

    except ValueError as e:
        print(e)


def main():
    want_to_quit = False
    task = ()
    while not want_to_quit:
        print_menu()
        user_choice = input('Que souhaitez-vous faire ?\n')
        if user_choice == 'quit':
            want_to_quit = True
        else:
            task = user_command(user_choice, task)


if __name__ == '__main__':
    main()
