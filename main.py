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
            task = add(task)
        elif message == 'done':
            task = done(task)
        elif message == 'update':
            task = update(task)
        elif message == 'list':
            list_not_done(task)
        elif message == 'list-done':
            list_done(task)
        elif message == 'list-all':
            list_all(task)
        else:
            raise Exception

    except Exception as e:
        message = "la commande n'existe pas"
        if e.__class__ == NotImplementedError:
            message = 'désolé vous ne pouvez pas utiliser cette fonction pour l\'instant'
        print(message)
    return task


def add(task):
    if task[0] != "":
        print(f'vous allez remplacer "{task[0]}"')
    print('saisissez le nom de votre tache')
    task_name = input()
    print(f'votre tache "{task_name}" a bien été ajoutée')
    return task_name, 'undone'


def done(task):
    if task[0] == '':
        print('Aucune tache trouvée')
        return task
    print('Votre tache est done')
    return task[0], 'done'


def update(task):
    if task[0] == '':
        print('Aucune tache trouvée')
        return task
    print(f'La tache porte le nom de {task[0]}, par quoi voulez-vous le remplacer ?')
    task_name = input()
    print('Le nom à bien été changé')
    return task_name, task[1]


def list_not_done(task):
    if task[1] == 'undone':
        print(task[0])
    else:
        print('pas de tâche non finie')


def list_done(task):
    if task[1] == 'done':
        print(task[0])
    else:
        print('pas de tache finie')


def list_all(task):
    print(task)


def main():
    task = ('', '')
    todo_list(task)


def todo_list(task):
    main_menu()
    response = input()
    if response != 'quit':
        task = user_input_handle(response, task)
        todo_list(task)


if __name__ == '__main__':
    main()

