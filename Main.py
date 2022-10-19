import todolist


class Main:

    def __init__(self):
        pass

    @classmethod
    def launch_todolist(cls):
        list_tasks = []
        user_input = ""

        while user_input != "quit":
            todolist.print_menu()
        print("hello")
# from todolist import print_menu
#
#
# class Main:
#     def __init__(self):
#         print("hello")
#
#     @classmethod
#     def launch_todolist(cls):
#         list_tasks = []
#         user_input = ""
#         while user_input != "quit":
# #             print_menu()
#             user_input = input("Please enter your command :")
#             list_tasks = do_action(list_tasks, user_input)
#         print("Goodbye")
#         print('╭∩╮(◉_◉)╭∩╮')
