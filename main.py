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


def user_input_handle(message, tasks):
    try:
        if message == 'add':
            tasks = add(tasks)
        elif message == 'done':
            tasks = done(tasks)
        elif message == 'update':
            tasks = update(tasks)
        elif message == 'list':
            list_not_done(tasks)
        elif message == 'list-done':
            list_done(tasks)
        elif message == 'list-all':
            list_all(tasks)
        else:
            raise Exception

    except Exception as e:
        message = "la commande n'existe pas"
        if e.__class__ == NotImplementedError:
            message = 'désolé vous ne pouvez pas utiliser cette fonction pour l\'instant'
        print(message)
    return tasks


def add(tasks):
    print('saisissez le nom de votre tache')
    task_name = input()
    print(f'votre tache "{task_name}" a bien été ajoutée')
    tasks.append((task_name, 'undone'))
    return tasks


def done(tasks):
    if len(tasks) == 0:
        print('Aucune tache trouvée')
        return tasks
    print('Votre tache est done')
    return tasks[0], 'done'


def update(tasks):
    if tasks[0] == '':
        print('Aucune tache trouvée')
        return tasks
    print(f'La tache porte le nom de {tasks[0]}, par quoi voulez-vous le remplacer ?')
    task_name = input()
    print('Le nom à bien été changé')
    return task_name, tasks[1]


def list_not_done(tasks):
    for task in tasks:
        if task[1] == 'undone':
            print(task[0])


def list_done(tasks):
    if tasks[1] == 'done':
        print(tasks[0])
    else:
        print('pas de tache finie')


def list_all(tasks):
    print(tasks)


def main():
    tasks = []
    todo_list(tasks)


def todo_list(tasks):
    main_menu()
    response = input()
    if response != 'quit':
        tasks = user_input_handle(response, tasks)
        todo_list(tasks)


if __name__ == '__main__':
    main()

