def add(tasks, task):
    user_task = input("Veuillez saisir votre nouvelle tâche")
    task = (user_task, False)
    tasks.append(task)
    print("tâche créée")
    return tasks, task


def done(tasks, task):
    index_tache = None
    while index_tache is None:
        try:
            list_all(tasks)
            index_tache = int(input("Indiquez le numéro de la tâche terminée")) - 1
        except Exception as err:
            print("entrée invalide : merci d'entrer un entier")
    if index_tache < 0 or index_tache + 1 > len(tasks):
        print("Cette tâche n'existe pas")
    else:
        task = (tasks[index_tache][0], True)
        tasks[index_tache] = task
        is_in_list = True
        print("tâche terminée")
    return tasks, task


def update(tasks, task):
    index_tache = None
    while index_tache is None:
        try:
            list_all(tasks)
            index_tache = int(input("Indiquez le numéro de la tâche à modifier")) - 1

        except Exception as err:
            print("entrée invalide : merci d'entrer un entier")
    if index_tache < 0 or index_tache + 1 > len(tasks):
        print("Cette tâche n'existe pas")
    else:
        nouveau_nom_tache = input("Veuillez saisir le nouveau nom de la tâche")
        task = (nouveau_nom_tache, tasks[index_tache][1])
        tasks[index_tache] = task
        print("tâche modifée")
    return tasks, task


def list(tasks):
    pending_tasks = []
    for item in tasks:
        if not item[1]:
            pending_tasks.append(item)
    if len(pending_tasks) > 0:
        print(pending_tasks)
    else:
        print("Aucune tâche finie pour l'instant!")


def list_done(tasks):
    done_tasks = []
    for item in tasks:
        if item[1]:
            done_tasks.append(item)
    if len(done_tasks) > 0:
        print(done_tasks)
    else:
        print("Aucune tâche finie pour l'instant!")


def list_all(tasks):
    done_tasks = []
    pending_tasks = []
    for index, task in enumerate(tasks):
        if task[1]:
            done_tasks.append((task, index))
        else:
            pending_tasks.append((task, index))
    if len(pending_tasks) > 0:
        print('Voici les tâches en cours')
        for task in pending_tasks:
            print(task[1] + 1, ":", task[0][0])
    if len(done_tasks) > 0:
        print('Voici les tâches terminées :')
        for task in done_tasks:
            print(task[1] + 1, ":", task[0][0])


def print_menu():
    print("voici le menu :")
    print("add       : Ajouter une tâche")
    print("done      : Effectuer une tâche")
    print("update    : Modifier le libellé d'une tâche")
    print("list      : Lister les tâches en cours")
    print("list-done : Lister les tâches terminées")
    print("list-all  : Lister toutes les tâches")
    print("quit      : Quitter")


def user_command(tasks, task, user_choice):
    try:
        if user_choice == 'add':
            tasks, task = add(tasks, task)
        elif user_choice == 'done':
            tasks, task = done(tasks, task)
        elif user_choice == 'update':
            tasks, task = update(tasks, task)
        elif user_choice == 'list':
            list(tasks)
        elif user_choice == 'list-done':
            list_done(tasks)
        elif user_choice == 'list-all':
            list_all(tasks)
        else:
            raise ValueError('La fonctionnalité n\'existe pas !')
    except ValueError as e:
        print(e)
    return tasks, task


def main():
    want_to_quit = False
    task = ()
    tasks = []
    print_menu()
    while not want_to_quit:
        user_choice = input('Que souhaitez-vous faire ?\n')
        if user_choice == 'quit':
            want_to_quit = True
        else:
            tasks, task = user_command(tasks, task, user_choice)


if __name__ == '__main__':
    main()
