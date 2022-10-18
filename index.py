def todo_list():
    menu()
    response = input()
    liste = []
    menu_handle = {'add': add, 'done': done, 'update': update, 'list': list_not_done, 'list-done': list_done,
                   'list-all': list_all}

    while response != "quit":
        try:
            menu_handle.get(response)(liste)

        except Exception as e:
            message = "la commande n'existe pas"
            if e.__class__ == NotImplementedError:
                message = 'désolé vous ne pouvez pas utiliser cette fonction pour l\'instant'

            print(e)
        menu()
        response = input()


def add(l):
    t = input("quelle tache souhaitez-vous ajouter ? \n")
    l.append((t, 0))


def done(l):
    list_not_done(l)
    r = int(input('entrer le numéro de tache a valider : ')) - 1
    l[r] = l[r][0], 1


def update(l):
    if len(l) == 0:
        print("il n'y a rien ici")
    else:
        list_all(l)
        r = int(input('entrer le numéro de tache a modifier : ')) - 1
        if r >= len(l):
            print("c'est pas bon")
            return l
        resp = input("Quel est le nouveau nom de votre tâche ?")
        l[r] = resp, l[r][1]


def list_not_done(l):
    has_no_tasks_not_done = True
    for idx, item in enumerate(l):
        if item[1] == 0:
            has_no_tasks_not_done = False
            print(item[0], 'tache n°:', idx + 1)
    if has_no_tasks_not_done:
        print('Aucune tâche à afficher')


def list_done(l):
    has_no_tasks_done = True
    for idx, item in enumerate(l):
        if item[1] == 1:
            has_no_tasks_done = False
            print(item[0], 'tache n°:', idx + 1)
    if has_no_tasks_done:
        print('Aucune tâche à afficher')


def list_all(l):
    print('en cours')
    list_not_done(l)
    print('terminé')
    list_done(l)


def menu():
    print(
        "Ajouter une tâche (add)"
        "\nEffectuer une tâche (done)"
        "\nModifier le libellé d'une tâche (update)"
        "\nLister les tâches en cours (list)"
        "\nLister les tâches terminées (list-done)"
        "\nLister toutes les tâches (list-all)"
        "\nQuitter (quit)")
    print("********Que voulez-vous faire ?**********")


def main():
    todo_list()


if __name__ == '__main__':
    main()
