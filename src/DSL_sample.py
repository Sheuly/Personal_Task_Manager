class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print("Invalid task index")

    def list_tasks(self):
        print("To-Do List:")
        for i, item in enumerate(self.tasks):
            status = " [X] " if item['completed'] else " [ ] "
            print(f"{i + 1}. {status} {item['task']}")


# DSL functions
def create_todo_list():
    return ToDoList()

def add_task(todo_list, task):
    todo_list.add_task(task)

def complete_task(todo_list, index):
    todo_list.complete_task(index - 1)

def list_tasks(todo_list):
    todo_list.list_tasks()

# Example usage
my_todo_list = create_todo_list()

add_task(my_todo_list, "Buy groceries")
add_task(my_todo_list, "Finish report")
add_task(my_todo_list, "Call Mom")

complete_task(my_todo_list, 1)  # Complete the first task

list_tasks(my_todo_list)
