def main():
    task = ("", "")
    tasks = []
    action = ask_action()
    while action != "quit":
        task = do_action(action, task, tasks)
        action = ask_action()
    print("Goodbye\n")


def done(tasks):
    index = int(input("Saissez le numéro de la tâche à clôturer (à partir de 0)"))
    done_task = (tasks[index][0], "Terminé")
    tasks[index] = done_task
    print(f'''Votre tâche: {tasks[index][0]} est à présent: {tasks[index][1]}''')
    print("******* Votre nouvelle liste de tâches :*******")
    for task in tasks:
        print(task[0], "=>", task[1])
    return tasks


def add(tasks):
    task = (input("Saisir la tache : "), "A faire")
    print(f'''Vous venez de créer la tache: 
        {task[0]}
        ''')
    tasks.append(task)
    print("tasks=>", tasks)
    return task, tasks


def update(tasks):
    index = int(input("Saissez le numéro de la tâche à modifier (à partir de 0)"))
    updated_task = (input("Veuillez renommer votre tâche"), tasks[index][1])
    tasks[index] = updated_task
    print("Votre tâche est renommée en :", updated_task[0])
    print("******* Votre nouvelle liste de tâches :*******")
    for task in tasks:
        print(task[0], "=>", task[1])
    return tasks


def display_list(tasks):
    print("******* Toutes vos tâches en cours: *******")
    pending_tasks = [task for task in tasks if task[1] == "A faire"]
    for task in pending_tasks:
        print(task[0], "=>", task[1])


def list_all(tasks):
    print("******* Toutes vos tâches: *******")
    for task in tasks:
        print(task[0], "=>", task[1])


def list_done(tasks):
    print("******* Toutes vos tâches terminées: *******")
    done_tasks = [task for task in tasks if task[1] == "Terminé"]
    print(done_tasks)


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


def do_action(commande, task, tasks):
    try:
        if commande == "add":
            task, tasks = add(tasks)
        elif commande == "done":
            tasks = done(tasks)
        elif commande == "update":
            tasks = update(tasks)
        elif commande == "list":
            display_list(tasks)
        elif commande == "list_done":
            list_done(tasks)
        elif commande == "all":
            list_all(tasks)
        else:
            raise ValueError("Commande inconnue\n")
    except(ValueError, NotImplementedError) as e:
        print(e)

    return task, tasks


if __name__ == "__main__":
    main()
