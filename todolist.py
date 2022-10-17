#menu
print("Bienvenue sur votre todolist. Que souhaitez vous faire?")


userInput = input(
                  "add => ajouter une tâche \n"
                  "done => marquer une tâche comme finie \n"
                  "update => modifier une tâche\n"
                  "list => lister les tâches en cours\n"
                  "list-done => lister les tâches terminées\n"
                  "list-all => lister toutes les tâches\n"
                  "quit => quitter l'application"
)


# Fonctions:
def add_task():
    raise ValueError()


def done_task():
    raise ValueError()


def update_task():
    raise ValueError()


def list_pending_tasks():
    raise ValueError()


def list_done_tasks():
    raise ValueError()


def list_all_tasks():
    raise ValueError()


def quit_todo_list():
    raise ValueError()


#dispatch
while userInput != "quit":
    try:
        if userInput == "add":
            add_task()
        elif userInput == "done":
            done_task()
        elif userInput == "update":
            update_task()
        elif userInput == "list":
            list_pending_tasks()
        elif userInput == "list-done":
            list_done_tasks()
        elif userInput == "list-all":
            list_all_tasks()
        elif userInput == "quit":
            quit_todo_list()
        else:
            print("Réponse invalide")
    except ValueError:
            print("La fonction de l'instruction ", userInput, "n'est pas encore implémentée")
    userInput = input(
        "add => ajouter une tâche \n"
        "done => marquer une tâche comme finie \n"
        "update => modifier une tâche\n"
        "list => lister les tâches en cours\n"
        "list-done => lister les tâches terminées\n"
        "list-all => lister toutes les tâches\n"
        "quit => quitter l'application")


