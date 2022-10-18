def main():
    action = ask_commande()
    while action != "quitter":
        do_commande(action)
        action = ask_commande()
    print("Goodbye\n")


def done():
    raise NotImplementedError("Commande non implémentée\n")


def add():
    raise NotImplementedError("Commande non implémentée\n")


def update():
    raise NotImplementedError("Commande non implémentée\n")


def display_list():
    raise NotImplementedError("Commande non implémentée\n")


def list_done():
    raise NotImplementedError("Commande non implémentée\n")


def list_all():
    raise NotImplementedError("Commande non implémentée\n")


def menu():
    print("Ajouter une linge : add ")
    print("Marquer comme éffectuée : done")
    print("Mettre à jour : update")
    print("Afficher la liste non éffectuées: display_list")
    print("Afficher list éffectuées : list-done")
    print("Afficher list tout : list-all")
    print("Quitter : quitter")


def ask_commande():
    menu()
    commande = input("\nEnter a command: ")
    return commande


def do_commande(commande):
    try:
        if commande == "add":
            add()
        elif commande == "done":
            done()
        elif commande == "update":
            update()
        elif commande == "display_list":
            display_list()
        elif commande == "list-done":
            list_done()
        elif commande == "list-all":
            list_all()
        else:
            raise ValueError("Commande inconnue\n")
    except(ValueError, NotImplementedError) as e:
        print(e)


if __name__ == "__main__":
    main()
