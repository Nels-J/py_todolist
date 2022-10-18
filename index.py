def todo_list():
    menu()
    response = ""
    tache = "", 0
    liste = []
    while response != "quit":
        response = input()
        try:
            if response == 'add':
                liste.append(add(tache))
                print(liste)
            elif response == 'done':
                liste = done(liste)
                print(liste)
            elif response == 'update':
                liste = update(liste)
                print(liste)
            elif response == 'list':
                list_not_done(liste)
            elif response == 'list-done':
                list_done(liste)
            elif response == 'list-all':
                list_all(liste)
            elif response == 'quit':
                return
            else:
                raise Exception

        except Exception as e:
            message = "la commande n'existe pas"
            if e.__class__ == NotImplementedError:
                message = 'désolé vous ne pouvez pas utiliser cette fonction pour l\'instant'

            print(e)
        menu()


def add(t):
    t = input("quelle tache souhaitez-vous ajouter ? \n")
    return t, 0


def done(l):
    list_not_done(l)
    r = int(input('entrer le numéro de tache a valider : ')) - 1
    print(l[r])
    l[r] = l[r][0], 1
    return l


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
    return l


def list_not_done(l):
    has_no_tasks_not_done = True
    for idx, item in enumerate(l):
        if item[1] == 0:
            has_no_tasks_not_done = False
            print(item[0], 'tache n°:', idx + 1 )
    if has_no_tasks_not_done:
        print('Aucune tâche à afficher')



def list_done(t):
    if t[1] == 1:
        return print(t[0])
    else:
        return print("aucune tache a afficher")


def list_all(l):
    for idx, item in enumerate(l):
        print(item[0], 'tache n°:', idx + 1)


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
