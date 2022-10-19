def main():
    tasks = []
    tasks = remplir_tasks(tasks)
    action = ask_action()
    while action != "quit":
        tasks = do_action(action, tasks)
        action = ask_action()
    print("Goodbye\n")


def add(tasks):
    tasks[0] = (input("Saisir la tache : "), False)
    print(f'''Vous venez de créer la tache: 
        {tasks[0][0]}
        ''')
    return tasks


def done(tasks):
    tasks[0] = (tasks[0][0], True)
    return tasks


def update(tasks):
    if tasks[0][0]:
        tasks[0] = (input(f'''Ancienne tâche : {tasks[0][0]}
            Modifier la tache : '''), tasks[0][1])
        print(f'''Vous venez de modifier la tache comme suit: 
            {tasks[0][0]}
            ''')
        return tasks
    else:
        print("Pas de tâche")


def list_pending(tasks):
    if not tasks[0][1]:
        print(tasks[0][0])


def list_done(tasks):
    if tasks[0][1]:
        print(tasks[0][0])


def list_all(tasks):
    list_pending(tasks)
    list_done(tasks)


def menu():
    print("Ajouter une ligne : add ")
    print("Marquer comme terminée : done")
    print("Mettre à jour : update")
    print("Afficher la liste des tâches non terminées: list")
    print("Afficher la liste des tâches terminées : list_done")
    print("Afficher toutes les tâches : list_all")
    print("Quitter : quit")


def ask_action():
    menu()
    commande = input("\nEnter a command: ")
    return commande


def do_action(command, tasks):
    try:
        if command == "add":
            tasks = add(tasks)
        elif command == "done":
            tasks = done(tasks)
        elif command == "update":
            tasks = update(tasks)
        elif command == "list":
            list_pending(tasks)
        elif command == "list_done":
            list_done(tasks)
        elif command == "list_all":
            list_all(tasks)
        else:
            raise ValueError("Commande inconnue\n")
    except(ValueError, NotImplementedError) as e:
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
