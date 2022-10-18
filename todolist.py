def main():
    task = ""
    action = ask_action()
    while action != "quitter":
        task = do_action(action, task)
        action = ask_action()
    print("Goodbye\n")


def done():
    raise NotImplementedError("Commande non implémentée\n")


def add():
    try:
        task = input("Saisir la tache : ")
        print(f'''Vous venez de créer la tache: 
        {task}
        ''')
        return task
    except:
        raise NotImplementedError("Commande non implémentée\n")


def update():
    raise NotImplementedError("Commande non implémentée\n")


def display_list(task):
    try:
        print(task)
    except:
        raise NotImplementedError("Commande non implémentée\n")


def list_done():
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


def do_action(commande, task):
    try:
        if commande == "add":
            task = add()
            return task
        elif commande == "done":
            done()
            return task
        elif commande == "update":
            update()
            return task
        elif commande == "list":
            display_list(task)
            return task
        elif commande == "list_done":
            list_done()
            return task
        elif commande == "all":
            list_all(task)
            return task
        else:
            raise ValueError("Commande inconnue\n")
    except(ValueError, NotImplementedError) as e:
        print(e)
        return task


if __name__ == "__main__":
    main()
