from exception import InvalidCommandException

class Menu:

    def __init__(self, tasks):
        self.menu_options = {
            "add": ("Ajouter une tâche", tasks.add_task),
            "update": ("Changer le nom d'une tâche", tasks.update_task_in_list),
            "done": ("Marquer une tâche comme terminée", tasks.mark_task_as_done_in_list),
            "list": ("Lister les tâches en cours", tasks.display_pending_tasks),
            "list_done": ("Lister les tâches terminées", tasks.display_done_tasks),
            "list_all": ("Lister toutes les tâches", tasks.display_all_tasks),
        }

    def do_action(self, command, interface_display, fichier):
        try:
            if command in self.menu_options.keys():
                return self.menu_options[command][1](interface_display, fichier)
            else:
                raise InvalidCommandException
        except InvalidCommandException as e:
            interface_display.print(e)

    def display(self, interface_display):
        for key, value in self.menu_options.items():
            interface_display.print(key + " : " + value[0])
