FILEPATH = "to-do.txt"


def get_todos(todos_path=FILEPATH):
    """
    Reads a text file and returns the list of to-do items
    """
    with open(todos_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the to-do items list in the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
