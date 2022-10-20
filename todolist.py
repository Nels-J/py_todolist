from module.tasks import Tasks
from module.ui import UI


class Application:

    def __init__(self):
        passa

    def start(self):
        menu = {
            "add": ("Ajouter une ligne", self.add),
            "done": ("Marquer comme terminée", self.done),
            "update": ("Mettre à jour", self.update),
            "list": ("Afficher la liste des tâches non terminées", self.list_pending),
            "list_done": ("Afficher la liste des tâches terminées", self.list_done),
            "list_all": ("Afficher toutes les tâches", self.list_all),
        }
        ui.print_menu(menu)
        action = ui.interact("\nQue souhaitez-vous faire ? ")
        while action != "quit":
            self.do_action(menu, action)
            action = ui.interact("\nQue souhaitez-vous faire ? ")
        ui.afficher("Goodbye\n")

    def add(self):
        label = ui.interact("Saisir le nom de la tache : ")
        tasks.add(label)
        ui.afficher("Tâche créée !")

    def done(self):
        self.list_pending()
        number = self.validate_user_input_number("terminer")
        tasks.list[number].done()
        ui.afficher(f'tache numéro {number} terminée')

    def update(self):
        self.list_all()
        number = self.validate_user_input_number("modifier")
        task_new_name = ui.interact("Entrez le nouveau nom de la tâche à modifier")
        tasks.list[number].update(task_new_name)
        ui.afficher(f'tache numéro {number} modifiée')

    def do_action(self, menu, command):
        try:
            if command in menu.keys():
                menu[command][1]()
            else:
                raise Exception("Commande inconnue")
        except Exception as e:
            ui.afficher(e)

    def list_pending(self):
        wanted_tasks_string = "en cours"
        wanted_tasks = tasks.list_pending()
        if len(wanted_tasks) > 0:
            ui.afficher(f'liste des tâches {wanted_tasks_string} :')
            for task in wanted_tasks:
                ui.afficher(f'{task[0]} : {task[1]}')
        else:
            ui.afficher(f'Pas de tâche  {wanted_tasks_string}')

    def list_done(self):
        wanted_tasks_string = "terminées"
        wanted_tasks = tasks.list_done()
        if len(wanted_tasks) > 0:
            ui.afficher(f'liste des tâches {wanted_tasks_string} :')
            for task in wanted_tasks:
                ui.afficher(f'{task[0]} : {task[1]}')
        else:
            ui.afficher(f'Pas de tâche  {wanted_tasks_string}')

    def list_all(self):
        self.list_pending()
        self.list_done()

    def validate_user_input_number(self, wanted_action):
        number = None
        list_index = []
        if wanted_action == "terminer":
            list_index = [index for index, task in enumerate(tasks.list) if not task.status]
        elif wanted_action == "modifier":
            list_index = [index for index, task in enumerate(tasks.list)]
        try:
            number = int(ui.interact("Quelle tâche voulez-vous " + wanted_action + " ?"))
            if number not in list_index:
                raise Exception("Le numéro que vous avez donné est invalide !")
        except Exception as e:
            ui.afficher(e)
            self.validate_user_input_number(wanted_action)
        return number


if __name__ == "__main__":
    tasks = Tasks()
    ui = UI()
    app = Application()
    app.start()
