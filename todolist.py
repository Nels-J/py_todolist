from display import InterfaceDisplay
from menu import Menu
from task import TasksList


class App:

    def start(self):
        interface_display = InterfaceDisplay()
        tasks = TasksList()
        fichier = open("tasks.txt", "w")
        fichier.write("Ma Todolist :" + "\n")
        fichier.close()
        menu = Menu(tasks)
        menu.display(interface_display)
        command = input("\nMerci de saisir une commande : ")
        while command != "quit":
            tasks.tasks_list = menu.do_action(command, interface_display)
            command = input("\nMerci de saisir une commande : ")
        interface_display.print("Goodbye!")


if __name__ == "__main__":
    app = App()
    app.start()
