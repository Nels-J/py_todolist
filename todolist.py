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



#dispatch
while userInput != "quit":
    try:
        if userInput == "add":
            raise ValueError()
        elif userInput == "done":
            raise ValueError()
        elif userInput == "update":
            raise ValueError()
        elif userInput == "list":
            raise ValueError()
        elif userInput == "list-done":
            raise ValueError()
        elif userInput == "list-all":
            raise ValueError()
        elif userInput == "quit":
            raise ValueError()
        else:
            print("Réponse invalide")
    except ValueError:
            print("La fonction de l'instruction ", userInput, "n'est pas encore implémentée")
            raise
    userInput = input(
        "add => ajouter une tâche \n"
        "done => marquer une tâche comme finie \n"
        "update => modifier une tâche\n"
        "list => lister les tâches en cours\n"
        "list-done => lister les tâches terminées\n"
        "list-all => lister toutes les tâches\n"
        "quit => quitter l'application")


