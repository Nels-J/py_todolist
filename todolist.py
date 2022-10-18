def main():
    task = ("", "")
    tasks = []
    action = ask_action()
    while action != "quit":
        task = do_action(action, task, tasks)
        action = ask_action()
    print("Goodbye\n")


def done(task, tasks):
    new_task = (task[0], "Terminé")
    return new_task, tasks


def add(tasks):
    task = (input("Saisir la tache : "), "A faire")
    print(f'''Vous venez de créer la tache: 
        {task[0]}
        ''')
    tasks.append(task)
    print("tasks=>", tasks)
    return task, tasks


def update(task, tasks):
    if task[0]:
        new_task = (input(f'''Ancienne tâche : {task[0]}
            Modifier la tache : '''), task[1])
        print(f'''Vous venez de modifier la tache comme suit: 
            {new_task[0]}
            ''')
        return new_task, tasks
    else:
        print("Pas de tâche")
        return task, tasks


def display_list(task, tasks):
    if task[1] == "A faire":
        print(task[0])


def list_all(task, tasks):
    print("******* Toutes vos tâches: *******")
    for task in tasks:
        print(task[0], "=>", task[1])


def list_done(task, tasks):
    if task[1] != "A faire":
        print(task[0])


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


def do_action(commande, task, tasks):
    try:
        if commande == "add":
            task, tasks = add(tasks)
        elif commande == "done":
            task, tasks = done(task, tasks)
        elif commande == "update":
            task, tasks = update(task, tasks)
        elif commande == "list":
            display_list(task, tasks)
        elif commande == "list_done":
            list_done(task, tasks)
        elif commande == "all":
            list_all(task, tasks)
        else:
            raise ValueError("Commande inconnue\n")
    except(ValueError, NotImplementedError) as e:
        print(e)

    return task, tasks


if __name__ == "__main__":
    main()
