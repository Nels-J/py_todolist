class Interface:

    def ask_action(self):
        return input(self.translate('Que souhaitez-vous faire ?\n'))

    def print_menu(self, menu):
        print("Voici le menu :")
        for cle, valeur in menu.items():
            print(cle, ":", valeur[0])
        print("quit : Quitter")

    def no_current_undone_task(self):
        print(self.translate("Aucune tâche en cours pour l'instant!"))

    def no_current_done_task(self):
        print(self.translate("Aucune tâche finie pour l'instant!"))

    def translate(self, text):
        return text

