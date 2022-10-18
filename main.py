def print_menu():
    print("voici le menu :")
    print("Ajouter une tâche (commande 'add')")
    print("Effectuer une tâche (commande 'done')")
    print("Modifier le libellé d'une tâche (commande 'update')")
    print("Lister les tâches en cours (commande 'list')")
    print("Lister les tâches terminées (commande 'list-done')")
    print("Lister toutes les tâches (commande 'list-all')")
    print("Quitter (command 'quit')")


def add():
    task_name = input("Quel est le nom de votre nouvelle tache ?")
    task_status = False
    return task_name, task_status


def done():
    print('VOUS AVEZ EFFECTUÉ VOTRE TÂCHE')
    return True


def update():
    new_name = input('Quel est le nouveau nom de votre tâche ?')
    return new_name


def list_in_progress(task_name, task_status):
    if not task_status:
        print(task_name)
    else:
        print('Aucune tâche en cours')


def list_done(task_name, task_status):
    if task_status:
        print(task_name)
    else:
        print('Aucune tâche terminée')


def list_all(task_name):
    print('Voicis toutes les tâches: \n' + task_name)


def user_input(user_choice, task_name, task_status):
    try:
        if user_choice == 'add':
            task_name, task_status = add()
        elif user_choice == 'done':
            task_status = done()
        elif user_choice == 'update':
            task_name = update()
        elif user_choice == 'list':
            list_in_progress(task_name, task_status)
        elif user_choice == 'list-done':
            list_done(task_name, task_status)
        elif user_choice == 'list-all':
            list_all(task_name)
        else:
            raise ValueError('La fonctionnalité n\'existe pas !')

    except ValueError as e:
        print(e)

    return task_name, task_status


def main():
    want_to_quit = False
    task_name = ""
    task_status = False
    while not want_to_quit:
        print_menu()
        user_choice = input('Que souhaitez-vous faire ?\n')
        if user_choice == 'quit':
            want_to_quit = True
        else:
            task_name, task_status = user_input(user_choice, task_name, task_status)


if __name__ == '__main__':
    main()
    print('╭∩╮(◉_◉)╭∩╮')
