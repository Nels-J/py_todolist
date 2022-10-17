def show_menu(todo_list):
    response = input('pour afficher votre dotolist : list \n'
                     'pour ajouter une tâche : add \n'
                     'pour modifier une tâche : update \n'
                     'pour lister les tâches en cours : list_done \n'
                     'pour check une tâche : done \n'
                     'pour quitter : quit ')
    if response == 'list':
        list_all(todo_list)
    elif response == 'add':
        add(todo_list)
    elif response == 'update':
        update(todo_list)
    elif response == 'list_done':
        list(todo_list)
    elif response == 'done':
        done(todo_list)
    elif response == 'quit':
        quit()
    else:
        show_menu(todo_list)


def add(todo_list):
    task_name = input('veuillez saisir le nom de votre tâche ?')
    todolist.append([task_name, 'en cours'])
    show_menu(todo_list)

def update(todo_list):
    pass


def list(todo_list):
    for task in todo_list:
        if task[1] == 'en cours':
            print(task[0])
    show_menu(todo_list)

def done(todo_list):
    pass


def quit():
    pass


def list_all(todolist):
    for task in todolist:
        print(task[0] + ": " + task[1])


todolist = [['Sortir le chat', 'en cours']]
show_menu(todolist)
