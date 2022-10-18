def print_menu():
    print("voici le menu :")
    print("Ajouter une tâche (commande 'add')")
    print("Effectuer une tâche (commande 'done')")
    print("Modifier le libellé d'une tâche (commande 'update')")
    print("Lister les tâches en cours (commande 'list')")
    print("Lister les tâches terminées (commande 'list-done')")
    print("Lister toutes les tâches (commande 'list-all')")
    print("Quitter (command 'quit')")


def add(tasks):
    task_name = input("Quel est le nom de votre nouvelle tache ?")
    task_status = False
    tasks.append((task_name, task_status))


def done(tasks):
    task_to_ckeck = input('Quelle tache souhaitez-vous accomplir ?')
    task_status = True
    tasks[int(task_to_ckeck) - 1] = (tasks[int(task_to_ckeck) - 1][0], task_status)


def update(tasks):
    task_to_update = input('Quelle tâche voulez vous modifier ?')
    new_name = input('Quel est le nouveau nom de votre tâche ?')
    tasks[int(task_to_update) - 1] = (new_name, tasks[int(task_to_update) - 1][1])


def list_in_progress(tasks):
    number_of_tasks_in_progress = 0
    for task in tasks:
        if not task[1]:
            number_of_tasks_in_progress += 1
            print(task[0])
    if number_of_tasks_in_progress == 0:
        print('Aucune tâche en cours')


def list_done(tasks):
    number_of_tasks_done = 0
    for task in tasks:
        if task[1]:
            number_of_tasks_done += 1
            print(task[0])
    if number_of_tasks_done == 0:
        print('Aucune tâche terminée')


def list_all(tasks):
    if len(tasks) == 0:
        print('Il n\'y a aucune tâches')

    tasks_in_progress = []
    tasks_done = []

    for task in tasks:
        if not task[1]:
            tasks_in_progress.append(task[0])
        else:
            tasks_done.append(task[0])
    if len(tasks_in_progress) > 0:
        print('Voici les tâches en cours: \n')
        for task_in_progress in tasks_in_progress:
            print(task_in_progress)
    else:
        print('Il n\'y a aucune tâches en cours')

    if len(tasks_done) > 0:
        print('\nVoici les tâches effectuées: \n')
        for task_done in tasks_done:
            print(task_done)
    else:
        print('Il n\'y a aucune tâches effectuée')


def user_input(user_choice, tasks: list):
    try:
        if user_choice == 'add':
            add(tasks)
        elif user_choice == 'done':
            done(tasks)
        elif user_choice == 'update':
            update(tasks)
        elif user_choice == 'list':
            list_in_progress(tasks)
        elif user_choice == 'list-done':
            list_done(tasks)
        elif user_choice == 'list-all':
            list_all(tasks)
        else:
            raise ValueError('La fonctionnalité n\'existe pas !')

    except ValueError as e:
        print(e)

    return tasks


def main():
    want_to_quit = False
    tasks: list = []
    while not want_to_quit:
        print_menu()
        user_choice = input('Que souhaitez-vous faire ?\n')
        if user_choice == 'quit':
            want_to_quit = True
        else:
            tasks = user_input(user_choice, tasks)


if __name__ == '__main__':
    main()
    print('╭∩╮(◉_◉)╭∩╮')
