from Task import Task


class TasksList:
    list = []

    def add(self, label):
        task = Task(label)
        self.list.append(task)

    def list_according_to_status(self, status):
        tasks = []
        for index, task in enumerate(self.list):
            if task.is_done == status:
                tasks.append((index, task))
        return tasks

    def print_task_list(self):
        string_list = ''
        for task in self.list:
            if task.is_done:
                string_list = string_list + '[X] ' + str(task.label) + '\n'
            else:
                string_list = string_list + '[ ] ' + str(task.label) + '\n'

        return string_list
