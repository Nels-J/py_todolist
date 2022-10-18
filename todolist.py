def main():
    task = "", "A faire"
    action = ask_action()
    while action != "quitter":
        task = do_action(action, task)
        action = ask_action()
    print("Goodbye\n")


def done(task):
    try:
        new_task = (task[0], "Terminé")
        return new_task
    except:
        raise NotImplementedError("Commande non implémentée\n")


def add():
    try:
        task = (input("Saisir la tache : "), "A faire")
        print(f'''Vous venez de créer la tache: 
        {task[0]}
        ''')
        return task
    except:
        raise NotImplementedError("Commande non implémentée\n")


def update(task):
    if task[0]:
        try:
            new_task = (input(f'''Ancienne tâche : {task[0]}
            Modifier la tache : '''), task[1])
            print(f'''Vous venez de modifier la tache comme suit: 
            {new_task[0]}
            ''')
            return new_task
        except:
            raise NotImplementedError("Commande non implémentée\n")
    else:
        print("Pas de tâche")


def display_list(task):
    if task[1] == "A faire":
        try:
            print(task[0])
        except:
            raise NotImplementedError("Commande non implémentée\n")


def list_all(task):
    try:
        print(task)
    except:
        raise NotImplementedError("Commande non implémentée\n")


def menu():
    print("Ajouter une linge : add ")
    print("Marquer comme éffectuée : done")
    print("Mettre à jour : update")
    print("Afficher la liste non éffectuées: list")
    print("Afficher list éffectuées : list_done")
    print("Afficher list tout : all")
    print("Quitter : quitter")


def ask_action():
    menu()
    commande = input("\nEnter a command: ")
    return commande


def list_done(task):
    if task[1] != "A faire":
        try:
            print(task[0])
        except:
            raise NotImplementedError("Commande non implémentée\n")


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
