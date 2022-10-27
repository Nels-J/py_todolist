class Interface:

    def ask_action(self):
        return input(self.translate('Que souhaitez-vous faire ?\n'))

    def print_menu(self, menu):
        print("Voici le menu :")
        for cle, valeur in menu.items():
            print(cle, ":", valeur[0])
        print("quit : Quitter")

    def translate(self, text):
        return text

    def no_undone_task(self):
        print(self.translate("Aucune tâche en cours pour l'instant!"))

    def no_done_task(self):
        print(self.translate("Aucune tâche finie pour l'instant!"))

    def done_tasks_are(self):
        print("Les tâches terminées sont :")

    def undone_tasks_are(self):
        print(self.translate("Les tâches en cours sont :"))

    def ask_new_task_name(self):
       return input("Veuillez saisir le nom de la tâche : ")

    def new_task_created(self):
        print("Tâche créée")

    def ask_nb_of_task_to_modify(self):
        return input("Indiquez le numéro de la tâche à modifier")

    def task_does_not_exist(self):
        print("Cette tâche n'existe pas")

    def modified_task_notification(self):
        print("Tâche modifée")

    def closed_task_notification(self):
        print("Tâche terminée")
    def ask_nb_of_task_to_close(self):
       return input("Indiquez le numéro de la tâche terminée : ")

    def display_task_with_nb(self, task):
        print(task[0] + 1, ":", task[1].label)
