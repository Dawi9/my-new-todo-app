def load_todos():
    """Load tasks from file and return them as a list."""
    try:
        with open("todos.txt", "r") as file:
            todos = [line.strip() for line in file.readlines()]
        return todos
    except FileNotFoundError:
        return []

def save_todos(todos):
    """Save tasks to file with numbering."""
    with open("todos.txt", "w") as file:
        for index, item in enumerate(todos, start=1):
            file.write(f"{index}. {item}\n")

todos = load_todos()

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ").strip()
            todos.append(todo)
            save_todos(todos)
            print(f"Added: {todo}")

        case 'show':
            todos = load_todos()
            if todos:
                for item in todos:
                    print(item)
            else:
                print("Your to-do list is empty.")

        case 'edit':
            try:
                number = int(input("Number of the todo to edit: "))
                todos = load_todos()
                if 1 <= number <= len(todos):
                    new_todo = input("Enter new todo: ").strip()
                    todos[number - 1] = new_todo
                    save_todos(todos)
                    print(f"Updated todo #{number} to: {new_todo}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        case 'complete':
            try:
                number = int(input("Number of the todo to complete: "))
                todos = load_todos()
                if 1 <= number <= len(todos):
                    removed = todos.pop(number - 1)
                    save_todos(todos)
                    print(f"Completed and removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        case 'exit':
            break

        case _:
            print("Invalid option. Please type add, show, edit, complete, or exit.")

print("Bye!")