def read_todos():
    try:
        with open('todos.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

def get_valid_index(prompt, todos):
    while True:
        try:
            number = int(input(prompt))
            if 1 <= number <= len(todos):
                return number - 1
            print(f"Please enter a number between 1 and {len(todos)}")
        except ValueError:
            print("Please enter a valid number")

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        if todo:  # Check if todo is not empty
            todos = read_todos()
            todos.append(todo + '\n')
            write_todos(todos)
        else:
            print("Todo cannot be empty")

    elif user_action == 'show':
        todos = read_todos()
        if not todos:
            print("No todos found")
        else:
            for index, item in enumerate(todos, 1):
                print(f"{index}-{item.strip()}")

    elif user_action == 'edit':
        todos = read_todos()
        if not todos:
            print("No todos to edit")
            continue
            
        index = get_valid_index("Number of the todo to edit: ", todos)
        new_todo = input("Enter new todo: ")
        if new_todo:  # Check if new todo is not empty
            todos[index] = new_todo + '\n'
            write_todos(todos)
        else:
            print("Todo cannot be empty")

    elif user_action == 'complete':
        todos = read_todos()
        if not todos:
            print("No todos to complete")
            continue
            
        index = get_valid_index("Number of the todo to complete: ", todos)
        removed_todo = todos.pop(index).strip()
        write_todos(todos)
        print(f"Todo '{removed_todo}' was removed from the list")

    elif user_action == 'exit':
        break
    else:
        print("Unknown command")

print("Bye!")