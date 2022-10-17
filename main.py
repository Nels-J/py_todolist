def main_menu():
    print(
        "Ajouter une tâche (add)"
        "\nEffectuer une tâche (done)"
        "\nModifier le libellé d'une tâche (update)"
        "\nLister les tâches en cours (list)"
        "\nLister les tâches terminées (list-done)"
        "\nLister toutes les tâches (list-all)"
        "\nQuitter (quit)")
    print("********Que voulez-vous faire ?**********")

    response = input()
    try:
        if response == 'add':
            add()
        elif response == 'done':
            done()
        elif response == 'update':
            update()
        elif response == 'list':
            list_not_done()
        elif response == 'list-done':
            list_done()
        elif response == 'list-all':
            list_all()
        elif response == 'quit':
            quit()
        else:
            raise Exception

    except Exception as e:
        message = "la commande n'existe pas"
        if e.__class__ == NotImplementedError:
            message = 'désolé vous ne pouvez pas utiliser cette fonction pour l\'instant'

        print(message)
    main_menu()


def add():
    raise NotImplementedError


def done():
    raise NotImplementedError


def update():
    raise NotImplementedError


def list_not_done():
    raise NotImplementedError


def list_done():
    raise NotImplementedError


def list_all():
    raise NotImplementedError


main_menu()
