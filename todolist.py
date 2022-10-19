def main():
    tasks = []
    action = ask_action()
    while action != "quit":
        tasks = do_action(action, tasks)
        action = ask_action()
    print("Goodbye\n")


def done(tasks):
    pending = []
    for task in tasks:
        if task[1] == "A faire":
            pending.append(task)
    if not pending:
        print('Pas de tâche')
    else:
        index = len(tasks)
        while index >= len(tasks):
            index = int(input("Saissez le numéro de la tâche à clôturer (à partir de 0)"))
            if index >= len(tasks):
                print("valeur incorrecte")
        tasks[index] = tasks[index][0], "Terminée"
        print(f'''Votre tâche: {tasks[index][0]} est à présent: {tasks[index][1]}''')
        list_all(tasks)
    return tasks


def add(tasks):
    task = (input("Saisir la tache : "), "A faire")
    print(f'''Vous venez de créer la tache: 
        {task[0]}
        ''')
    tasks.append(task)
    print("tasks=>", tasks)
    return tasks


def update(tasks):
    if not tasks:
        print('Pas de tâche')
    else:
        index = len(tasks)
        while index >= len(tasks):
            index = int(input("Saissez le numéro de la tâche à renommer (à partir de 0)"))
            if index >= len(tasks):
                print("valeur incorrecte")
        tasks[index] = input("Veuillez renommer votre tâche"), tasks[index][1]
        print("Votre tâche est renommée en :", tasks[index][0])
        list_all(tasks)
    return tasks


def display_list(tasks):
    print("******* Toutes vos tâches en cours: *******")
    for task in tasks:
        if task[1] == "A faire":
            print(task[0], "=>", task[1])


def list_all(tasks):
    print("******* Toutes vos tâches: *******")
    display_list(tasks)
    list_done(tasks)


def list_done(tasks):
    print("******* Toutes vos tâches terminées: *******")
    for task in tasks:
        if task[1] == "Terminée":
            print(task[0], "=>", task[1])


def menu():
    print("Ajouter une ligne : add ")
    print("Marquer comme terminée : done")
    print("Mettre à jour : update")
    print("Afficher la liste des tâches non terminées: list")
    print("Afficher la liste des tâches terminées : list_done")
    print("Afficher toutes les tâches : all")
    print("Quitter : quit")


def ask_action():
    menu()
    commande = input("\nEnter a command: ")
    return commande


def do_action(commande, tasks):
    try:
        if commande == "add":
            tasks = add(tasks)
        elif commande == "done":
            tasks = done(tasks)
        elif commande == "update":
            tasks = update(tasks)
        elif commande == "list":
            display_list(tasks)
        elif commande == "list_done":
            list_done(tasks)
        elif commande == "all":
            list_all(tasks)
        else:
            raise ValueError("Commande inconnue\n")
    except(ValueError, NotImplementedError) as e:
        print(e)

    return tasks


if __name__ == "__main__":
    main()
