def main():
    tasks = []
    tasks = remplir_tasks(tasks)
    menu = {
        "add": ("Ajouter une ligne", add),
        "done": ("Marquer comme terminée", done),
        "update": ("Mettre à jour", update),
        "list": ("Afficher la liste des tâches non terminées", list_pending),
        "list_done": ("Afficher la liste des tâches terminées", list_done),
        "list_all": ("Afficher toutes les tâches", list_all),
    }
    print_menu(menu)
    action = input("\nQue souhaitez-vous faire ? ")
    while action != "quit":
        tasks = do_action(menu, action, tasks)
        action = input("\nQue souhaitez-vous faire ? ")
    print("Goodbye\n")


def add(tasks):
    tasks.append((input("Saisir le nom de la tache : "), False))
    print("Tâche créée !")
    return tasks


def validate_user_input_number(tasks, wanted_action):
    number = None
    list_index = []
    if wanted_action == "terminer":
        list_index = [index for index, task in enumerate(tasks) if not task[1]]
    elif wanted_action == "modifier":
        list_index = [index for index, task in enumerate(tasks)]
    try:
        number = int(input("Quelle tâche voulez-vous " + wanted_action + " ?"))
        if number not in list_index:
            raise Exception("Le numéro que vous avez donné est invalide !")
    except Exception as e:
        print(e)
        validate_user_input_number(tasks, wanted_action)
    return number


def done(tasks):
    list_pending(tasks)
    number = validate_user_input_number(tasks, "terminer")
    tasks[number] = (tasks[number][0], True)
    print("tache numéro", number, "terminée")
    return tasks


def update(tasks):
    list_all(tasks)
    number = validate_user_input_number(tasks, "modifier")
    task_new_name = input("Entrez le nouveau nom de la tâche à modifier")
    tasks[number] = (task_new_name, tasks[number][1])
    print("tache numéro", number, "modifiée")
    return tasks


def list_wanted_tasks(tasks, wanted_status, wanted_tasks_string):
    wanted_tasks = []
    for index, task in enumerate(tasks):
        if task[1] == wanted_status:
            wanted_tasks.append((index, task[0]))
    if len(wanted_tasks) > 0:
        print("liste des tâches", wanted_tasks_string, " :")
        for task in wanted_tasks:
            print(task[0], " : ", task[1])
    else:
        print("Pas de tâche ", wanted_tasks_string)
    return wanted_tasks


def list_pending(tasks):
    # refacto
    # wanted_status = False
    # wanted_tasks_string = "en cours"
    # list_wanted_tasks(tasks, wanted_status, wanted_tasks_string)
    list_wanted_tasks(tasks, False, "en cours")


def list_done(tasks):
    # refacto
    # wanted_status = True
    # wanted_tasks_string = "terminées"
    # list_wanted_tasks(tasks, wanted_status, wanted_tasks_string)
    list_wanted_tasks(tasks, True, "terminées")


def list_all(tasks):
    list_pending(tasks)
    list_done(tasks)


def print_menu(menu):
    for key, value in menu.items():
        print("--", key, "=>", value[0], )
    print("quit :  Quitter ")


def do_action(menu, command, tasks):
    try:
        if command in menu.keys():
            menu[command][1](tasks)
        else:
            raise Exception("Commande inconnue")
    except Exception as e:
        print(e)
    return tasks


def remplir_tasks(tasks):
    tasks.append(("Manger", False))
    tasks.append(("Boire", True))
    tasks.append(("Travailler", False))
    tasks.append(("Dormir", True))
    tasks.append(("Marcher", False))
    tasks.append(("Courir", True))
    return tasks


if __name__ == "__main__":
    main()
