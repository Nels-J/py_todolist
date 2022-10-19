class CLUI:

    def display(self):
        print("Ajouter une ligne : add ")
        print("Marquer comme terminée : done")
        print("Mettre à jour : update")
        print("Afficher la liste des tâches non terminées: list")
        print("Afficher la liste des tâches terminées : list_done")
        print("Afficher toutes les tâches : all")
        print("Quitter : quit")

    def print(self, message):
        print(message)


class InvalidCommandException(Exception):
    def __init__(self):
        super().__init__("Commande invalide")


class InvalidValueException(Exception):
    def __init__(self):
        super().__init__("Valeur invalide")


def main():
    cli = CLUI()

    menu = {
        "add": ("Ajouter une tâche", "add", add),
        "update": ("Changer le nom d'une tâche", "update", update),
        "done": ("Marquer une tâche comme terminée", "done", done),
        "list": ("Lister les tâches en cours", "list", display_list),
        "list_done": ("Lister les tâches terminées", "list_done", list_done),
        "list_all": ("Lister toutes les tâches", "list_all", list_all),
    }

    tasks = []
    cli.display()
    action = input("\nEnter a command: ")
    while action != "quit":
        tasks = do_action(action, tasks, menu, cli)
        action = input("\nEnter a command: ")
    cli.print("Goodbye!")


def done(tasks, cli):
    pending = []
    for task in tasks:
        if task[1] == "A faire":
            pending.append(task)
    if not pending:
        cli.no_tasks()
    else:
        index = len(tasks)
        while index >= len(tasks):
            try:
                index = int(input("Saissez le numéro de la tâche à clôturer (à partir de 0)"))
                if index >= len(tasks):
                    raise InvalidValueException
            except InvalidValueException as e:
                cli.print(e)
        tasks[index] = tasks[index][0], "Terminée"
        cli.print(f'Votre tâche: {tasks[index][0]} est à présent: {tasks[index][1]}')
        list_all(tasks, cli)
    return tasks


def add(tasks, cli):
    task = (input("Saisir la tache : "), "A faire")
    cli.print(f'Vous venez de créer la tache: {task[0]}')
    tasks.append(task)
    cli.print(f"tasks=> {tasks}")
    return tasks


def update(tasks, cli):
    if not tasks:
        cli.print("Pas de tâche à afficher")
    else:
        index = len(tasks)
        while index >= len(tasks):
            try:
                index = int(input("Saissez le numéro de la tâche à renommer (à partir de 0)"))
                if index >= len(tasks):
                    raise InvalidValueException
            except InvalidValueException as e:
                cli.print(e)
        tasks[index] = input("Veuillez renommer votre tâche"), tasks[index][1]
        cli.print(f"Votre tâche est renommée en : {tasks[index][0]}")
        list_all(tasks, cli)
    return tasks


def display_list(tasks, cli):
    cli.print("******* Toutes vos tâches en cours: *******")
    for task in tasks:
        if task[1] == "A faire":
            cli.print(f"{task[0]} => {task[1]}")
    return tasks


def list_all(tasks, cli):
    cli.print("******* Toutes vos tâches: *******")
    display_list(tasks, cli)
    list_done(tasks, cli)
    return tasks


def list_done(tasks, cli):
    cli.print("******* Toutes vos tâches terminées: *******")
    for task in tasks:
        if task[1] == "Terminée":
            cli.print(f"{task[0]} => {task[1]}")
    return tasks


def do_action(commande, tasks, menu, cli):
    try:
        if commande in menu:
            tasks = menu[commande][2](tasks, cli)
        else:
            raise InvalidCommandException
    except InvalidCommandException as e:
        cli.print(e)
    return tasks


if __name__ == "__main__":
    main()
