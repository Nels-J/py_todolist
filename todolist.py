from Tasks import Tasks
from UI import UI


def main():
    menu = {
        "add": ("Ajouter une ligne", add),
        "done": ("Marquer comme terminée", done),
        "update": ("Mettre à jour", update),
        "list": ("Afficher la liste des tâches non terminées", list_pending),
        "list_done": ("Afficher la liste des tâches terminées", list_done),
        "list_all": ("Afficher toutes les tâches", list_all),
    }
    UI.print_menu(menu)
    action = UI.interact("\nQue souhaitez-vous faire ? ")
    while action != "quit":
        tasks = do_action(menu, action)
        action = UI.interact("\nQue souhaitez-vous faire ? ")
    UI.afficher("Goodbye\n")


def update():
    pass


def done():
    pass


def list_all():
    list_pending()
    list_done()


def list_pending():
    wanted_tasks_string = "en cours"
    wanted_tasks = tasks.list_pending()
    if len(wanted_tasks) > 0:
        UI.afficher(f'liste des tâches {wanted_tasks_string} :')
        for task in wanted_tasks:
            UI.afficher(f'{task[0]} : {task[1]}')
    else:
        UI.afficher(f'Pas de tâche  {wanted_tasks_string}')


def list_done():
    wanted_tasks_string = "terminées"
    wanted_tasks = tasks.list_done()
    if len(wanted_tasks) > 0:
        UI.afficher(f'liste des tâches {wanted_tasks_string} :')
        for task in wanted_tasks:
            UI.afficher(f'{task[0]} : {task[1]}')
    else:
        UI.afficher(f'Pas de tâche  {wanted_tasks_string}')


def add():
    label = UI.interact("Saisir le nom de la tache : ")
    tasks.add(label)
    UI.afficher("Tâche créée !")


def do_action(menu, command):
    try:
        if command in menu.keys():
            menu[command][1]()
        else:
            raise Exception("Commande inconnue")
    except Exception as e:
        UI.afficher(e)
        raise
    return tasks


def remplir_tasks(tasks):
    tasks.append(("Manger", False))
    tasks.append(("Boire", True))
    tasks.append(("Travailler", False))
    tasks.append(("Dormir", True))
    tasks.append(("Marcher", False))
    tasks.append(("Courir", True))
    return tasks


if __name__ == "__main__":
    tasks = Tasks()
    UI = UI()
    main()
