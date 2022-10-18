def main():
    task = ("", "")
    action = ask_action()
    while action != "quit":
        task = do_action(action, task)
        action = ask_action()
    print("Goodbye\n")


def done(task):
    new_task = (task[0], "Terminé")
    return new_task


def add():
    task = (input("Saisir la tache : "), "A faire")
    print(f'''Vous venez de créer la tache: 
        {task[0]}
        ''')
    return task


def update(task):
    if task[0]:
        new_task = (input(f'''Ancienne tâche : {task[0]}
            Modifier la tache : '''), task[1])
        print(f'''Vous venez de modifier la tache comme suit: 
            {new_task[0]}
            ''')
        return new_task
    else:
        print("Pas de tâche")


def display_list(task):
    if task[1] == "A faire":
        print(task[0])


def list_all(task):
    print(task)


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


def list_done(task):
    if task[1] != "A faire":
        print(task[0])


def do_action(commande, task):
    try:
        if commande == "add":
            task = add()
        elif commande == "done":
            task = done(task)
        elif commande == "update":
            task = update(task)
        elif commande == "list":
            display_list(task)
        elif commande == "list_done":
            list_done(task)
        elif commande == "all":
            list_all(task)
        else:
            raise ValueError("Commande inconnue\n")
    except(ValueError, NotImplementedError) as e:
        print(e)

    return task


if __name__ == "__main__":
    main()
