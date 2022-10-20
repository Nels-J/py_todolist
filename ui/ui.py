class UI:

    def afficher(self, message):
        print(message)

    def interact(self, message):
        return input(message)

    def print_menu(self, menu_object):
        for key, value in menu_object.items():
            self.afficher(f'-- {key} => {value[0]}')
        self.afficher("quit :  Quitter ")
