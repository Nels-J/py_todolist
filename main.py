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


def user_input_handle(message, task):
    try:
        if message == 'add':
            return add(task)
        elif message == 'done':
            done()
        elif message == 'update':
            update()
        elif message == 'list':
            list_not_done()
        elif message == 'list-done':
            list_done()
        elif message == 'list-all':
            list_all()
        else:
            raise Exception

    except Exception as e:
        message = "la commande n'existe pas"
        if e.__class__ == NotImplementedError:
            message = 'désolé vous ne pouvez pas utiliser cette fonction pour l\'instant'
        print(message)


def add(task):
    if task != "":
        print(f'vous allez remplacer "{task}"')
    print('saisissez le nom de votre tache')
    task = input()
    print(f'votre tache "{task}" a bien été ajoutée')
    return task

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


def main():
    task = ''
    todo_list(task)


def todo_list(task):
    main_menu()
    response = input()
    if response != 'quit':
        task = user_input_handle(response, task)
        todo_list(task)


if __name__ == '__main__':
    main()

