FILEPATH = "todo.txt"
def get_todos(filepath=FILEPATH):
    """
    Read a text files and return a list of
    to-do items.
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

#1
def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write  a list of to-do items to a text file.
    """
    with open(filepath,'w') as file:
            todos_local = file.writelines(todos_arg)
    return todos_local
if __name__ == "__Todo__":
    print("hello")
    print(get_todos())