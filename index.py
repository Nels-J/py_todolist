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
                list_not_done(tache)
            elif response == 'list-done':
                list_done(tache)
            elif response == 'list-all':
                list_all(tache)
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
    for idx, name in enumerate(l):
        print(name[0], 'tache n°:', idx+1, )

    r = int(input('entrer le numéro de tache a valider : '))-1
    print(l[r])
    l[r] = l[r][0], 1
    return l


def update(l):
    print(l)
    for idx, name in enumerate(l):
        print(f'{name[0]} tache n° {idx + 1 }')

    r = int(input('entrer le numéro de tache a modifier : ')) - 1
    resp = input("Quel est le nouveau nom de votre tâche ?")
    l[r] = resp, l[r][1]
    return l



def list_not_done(t):
    if t[1] == 0:
        return print(t[0])
    else:
        return print("aucune tache a afficher")


def list_done(t):
    if t[1] == 1:
        return print(t[0])
    else:
        return print("aucune tache a afficher")


def list_all(t):
    return print(t[0])


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