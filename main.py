def add(tasks):
    user_task = input("Veuillez saisir votre nouvelle tâche: ")
    task = (user_task, False)
    tasks = add_to_list(tasks, task)
    print("Tâche créée")
    return tasks


def add_to_list(tasks, task):
    tasks.append(task)
    return tasks


def done(tasks):
    index_tache = None
    while index_tache is None:
        try:
            list_all(tasks)
            index_tache = int(input("Indiquez le numéro de la tâche terminée : ")) - 1
        except Exception as err:
            print("Entrée invalide : merci d'entrer un entier")
    if index_tache < 0 or index_tache + 1 > len(tasks):
        print("Cette tâche n'existe pas")
    else:
        task = (tasks[index_tache][0], True)
        tasks[index_tache] = task
        is_in_list = True
        print("Tâche terminée")
    return tasks


def update(tasks):
    index_tache = None
    while index_tache is None:
        try:
            list_all(tasks)
            index_tache = int(input("Indiquez le numéro de la tâche à modifier")) - 1

        except Exception as err:
            print("Entrée invalide : merci d'entrer un entier")
    if index_tache < 0 or index_tache + 1 > len(tasks):
        print("Cette tâche n'existe pas")
    else:
        nouveau_nom_tache = input("Veuillez saisir le nouveau nom de la tâche")
        task = (nouveau_nom_tache, tasks[index_tache][1])
        tasks[index_tache] = task
        print("Tâche modifée")
    return tasks


def list(tasks):
    pending_tasks = []
    for index, item in enumerate(tasks):
        if not item[1]:
            pending_tasks.append((index, item))
    if len(pending_tasks) > 0:
        print("Les tâches en cours sont :")
        for pending_task in pending_tasks:
            print(pending_task[0] + 1, ":", pending_task[1][0])
    else:
        print("Aucune tâche en cours pour l'instant!")


def list_done(tasks):
    done_tasks = []
    for index, item in enumerate(tasks):
        if item[1]:
            done_tasks.append((index, item))
    if len(done_tasks) > 0:
        print("Les tâches terminées sont :")
        for done_task in done_tasks:
            print(done_task[0] + 1, ":", done_task[1][0])
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
        print('Voici les tâches en cours :')
        for task in pending_tasks:
            print(task[1] + 1, ":", task[0][0])
    if len(done_tasks) > 0:
        print('Voici les tâches terminées :')
        for task in done_tasks:
            print(task[1] + 1, ":", task[0][0])


def print_menu(menu):
    print("Voici le menu :")
    # print("add       : Ajouter une tâche")
    # print("done      : Effectuer une tâche")
    # print("update    : Modifier le libellé d'une tâche")
    # print("list      : Lister les tâches en cours")
    # print("list-done : Lister les tâches terminées")
    # print("list-all  : Lister toutes les tâches")
    for cle, valeur in menu.items():
        print(cle, ":", valeur[0])
    print("quit : Quitter")


def is_valid(user_choice, menu):
    if user_choice in menu:
        return True
    else:
        return False


def user_command(tasks, user_choice, menu):
    try:
        if is_valid(user_choice, menu):
            menu[user_choice][1](tasks)
        else:
            raise ValueError('La fonctionnalité n\'existe pas !')
    except ValueError as e:
        print(e)
    return tasks


def scenario(tasks):
    add_to_list(tasks, ("t1", False))
    add_to_list(tasks, ("t2", False))
    return tasks

def main():
    want_to_quit = False
    task = ()
    tasks = []
    menu = {"add": ("Ajouter une tâche", add),
            "done": ("Effectuer une tâche", done),
            "update": ("Modifier le libellé d'une tâche", update),
            "list": ("Lister les tâches en cours", list),
            "list-done": ("Lister les tâches terminées", list_done),
            "list-all": ("Lister toutes les tâches", list_all),
            "test": ("test", scenario)
            }
    print_menu(menu)
    while not want_to_quit:
        user_choice = input('Que souhaitez-vous faire ?\n')
        if user_choice == 'quit':
            want_to_quit = True
        else:
            tasks = user_command(tasks, user_choice, menu)


if __name__ == '__main__':
    main()
