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
def add(input):
    try:
        print("la fonction 'add()' n'est pas encore implémentée pour: ", input)
    except Exception as e:
        print(e)

#dispatch
while userInput != "quit":
    if userInput == "add":
       add(userInput)
    elif userInput == "done":
       print("done")
    elif userInput == "update":
       print("update")
    elif userInput == "list":
       print("list")
    elif userInput == "list-done":
       print("list-done")
    elif userInput == "list-all":
       print("list-all")
    elif userInput == "quit":
       print("quit")
    else:
       print("Invalid answer")
    userInput = input(
        "add => ajouter une tâche \n"
        "done => marquer une tâche comme finie \n"
        "update => modifier une tâche\n"
        "list => lister les tâches en cours\n"
        "list-done => lister les tâches terminées\n"
        "list-all => lister toutes les tâches\n"
        "quit => quitter l'application")

