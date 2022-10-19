class UI:

    def afficher(self, message):
        print(message)

    def interact(self, message):
        return input(message)

    def print_menu(self, menu_object):
        for key, value in menu_object.items():
            self.afficher(f'-- {key} => {value[0]}')
        self.afficher("quit :  Quitter ")

    def print_list_tasks(self, tasks, wanted_tasks_string):
        self.afficher(f'liste des tâches {wanted_tasks_string} :')
        for task in tasks:
            self.afficher(f'{task[0]} : {task[1]}')
