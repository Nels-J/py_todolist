def done():
    raise NotImplementedError("commande non implémentée")


def add():
    raise NotImplementedError("commande non implémentée")


def update():
    raise NotImplementedError("commande non implémentée")


def display_list():
    raise NotImplementedError("commande non implémentée")


def list_done():
    raise NotImplementedError("commande non implémentée")


def list_all():
    raise NotImplementedError("commande non implémentée")


def quitter():
    raise SystemExit



def menu():
    print("Ajouter une linge : add ")
    print("Marquer comme éffectuée : done")
    print("Mettre à jour : update")
    print("Afficher la liste non éffectuées: display_list")
    print("Afficher list éffectuées : list-done")
    print("Afficher list tout : list-all")
    print("Quitter : quitter")





def main():
    menu()
    commande = input("Enter a command: ")
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
        elif commande == "quitter":
            quitter()
        else:
            raise ValueError("Commande inconnue")
    except(ValueError, NotImplementedError)as e:
        print(e)
    main()


main()


