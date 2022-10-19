from UI import UI


class Task:
    label = None
    status = False

    def __init__(self, label):
        self.label = label

    def validate_user_input_number(self, tasks, wanted_action):
        number = None
        list_index = []
        if wanted_action == "terminer":
            list_index = [index for index, task in enumerate(tasks) if not task[1]]
        elif wanted_action == "modifier":
            list_index = [index for index, task in enumerate(tasks)]
        try:
            number = int(UI.interact("Quelle tâche voulez-vous " + wanted_action + " ?"))
            if number not in list_index:
                raise Exception("Le numéro que vous avez donné est invalide !")
        except Exception as e:
            UI.afficher(e)
            self.validate_user_input_number(tasks, wanted_action)
        return number

    def done(self, tasks):
        list_pending(tasks)
        number = self.validate_user_input_number(tasks, "terminer")
        tasks[number] = (tasks[number][0], True)
        UI.afficher(f'tache numéro {number} terminée')
        return tasks

    def update(self, tasks):
        list_all(tasks)
        number = self.validate_user_input_number(tasks, "modifier")
        task_new_name = UI.interact("Entrez le nouveau nom de la tâche à modifier")
        tasks[number] = (task_new_name, tasks[number][1])
        UI.afficher(f'tache numéro {number} modifiée')
        return tasks
