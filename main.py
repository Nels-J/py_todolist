def print_menu():
    print("voici le menu :")
    print("Ajouter une tâche (commande 'add')")
    print("Effectuer une tâche (commande 'done')")
    print("Modifier le libellé d'une tâche (commande 'update')")
    print("Lister les tâches en cours (commande 'list')")
    print("Lister les tâches terminées (commande 'list-done')")
    print("Lister toutes les tâches (commande 'list-all')")
    print("Quitter (command 'quit')")


def add(tasks):
    task_name = input("Quel est le nom de votre nouvelle tache ?")
    task_status = False
    tasks.append((task_name, task_status))


def done(tasks):
    task_to_ckeck = input('Quelle tache souhaitez-vous accomplir ?')
    task_status = True
    tasks[int(task_to_ckeck) - 1] = (tasks[int(task_to_ckeck) - 1][0], task_status)


def update(tasks):
    task_to_update = input('Quelle tâche voulez vous modifier ?')
    new_name = input('Quel est le nouveau nom de votre tâche ?')
    tasks[int(task_to_update) - 1] = (new_name, tasks[int(task_to_update) - 1][1])


def list_in_progress(tasks):
    print('Liste des tâches en cours:')
    number_of_tasks_in_progress = 0
    for count, task in enumerate(tasks):
        if not task[1]:
            number_of_tasks_in_progress += 1
            print(count + 1, '-', task[0])
    if number_of_tasks_in_progress == 0:
        print('Aucune tâche en cours')


def list_done(tasks):
    print('Liste des tâches terminées:')
    number_of_tasks_done = 0
    for count, task in enumerate(tasks):
        if task[1]:
            number_of_tasks_done += 1
            print(count + 1, '-', task[0])
    if number_of_tasks_done == 0:
        print('Aucune tâche terminée')


def list_all(tasks):
    list_in_progress(tasks)
    list_done(tasks)


def user_input(user_choice: str, tasks: list):
    choices = {
        'add': (print_menu, add),
        'done': (print_menu, done),
        'update': (print_menu, update),
        'list': (print_menu, list_in_progress),
        'list-done': (print_menu, list_done),
        'list-all': (print_menu, list_all),
    }
    choices[user_choice][0]
    choices[user_choice][1](tasks)
    return tasks


def main():
    want_to_quit = False
    tasks: list = []
    while not want_to_quit:
        print_menu()
        user_choice = input('Que souhaitez-vous faire ?\n')
        if user_choice == 'quit':
            want_to_quit = True
        else:
            tasks = user_input(user_choice, tasks)


if __name__ == '__main__':
    main()
    print('╭∩╮(UwU)╭∩╮')
