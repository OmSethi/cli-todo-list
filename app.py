# cli todolist
# cool quick personal project


# list of tasks



tasks = []

def cli_menu():
    print("""
===== CLI-TO-DO LIST =====
1. View Tasks
2. Add Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
""")

def add_task():
    new_task = input("Enter a new task")
    tasks.append(new_task)


            