def menu():
    print("Bienvenue sur votre ToDoList :) Les commandes disponibles :")
    print("Veuillez taper   'add'         pour ajouter un élément à la ToDoList")
    print("Veuillez taper   'done'        pour cocher un élément à la ToDoList")
    print("Veuillez taper   'update'      pour metre à jour un élément de la ToDoList")
    print("Veuillez taper   'list'        pour lister les éléments en cours de la ToDoList")
    print("Veuillez taper   'list-done'   pour lister les éléments cochés de la ToDoList")
    print("Veuillez taper   'list-all'    pour lister tous les éléments de la ToDoList")
    print("Veuillez taper   'quit'        pour quitter")


def add():
    raise Exception()


def done():
    raise Exception()


def update():
    raise Exception()


def liste():
    raise Exception()


def list_done():
    raise Exception()


def list_all():
    raise Exception()


def quit():
    raise Exception()


def check_input(userInput):
    try:
        if userInput == "add":
            add()
        elif userInput == 'done':
            done()
        elif userInput == 'update':
            update()
        elif userInput == 'list':
            liste()
        elif userInput == 'list-done':
            list_done()
        elif userInput == 'list-all':
            list_all()
        elif userInput == 'quit':
            quit()

    except Exception:
        print("Nous sommes désolé, Cette commande n'est pas encore implémentée")
    toDoList()


def toDoList():
    menu()
    userInput = input()
    check_input(userInput)


toDoList()