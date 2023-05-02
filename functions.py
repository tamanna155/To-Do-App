def get_todos():
    """Read a text file and returns the list
    of to-do items.
    """
    with open("todos.txt", 'r') as files:
        todoo = files.readlines()
    return todoo


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as files:
        files.writelines(todos_arg)
