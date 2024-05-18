class Task:
    def __init__(self, description):
        self.description = description


class TaskPerformance:
    def __init__(self):
        self.tasks = []

    def add(self, description):
        self.tasks.append(Task(description))
        return f"Task added: {description}"

    def delete(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            return "Task deleted"
        else:
            return "Not deleted"


# DSL functions
def create_list():
    return TaskPerformance()

def add_task(task_list, description):
    message = task_list.add(description)
    print(message)

def delete_task(task_list, index):
    message = task_list.delete(index - 1)
    print(message)



# Example usage
act = create_list()
add_task(act, "Write blog post")
add_task(act, "Clean the house")
add_task(act, "Pay bills")
delete_task(act, 2)


