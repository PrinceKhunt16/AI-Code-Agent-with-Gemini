def add_todo(todos, task):
    todos.append(task)
    print(f"Added todo: {task}")

def list_todos(todos):
    if not todos:
        print("No todos yet!")
    else:
        for i, task in enumerate(todos):
            print(f"{i+1}. {task}")

def remove_todo(todos, index):
    try:
        index = int(index) - 1
        removed_todo = todos.pop(index)
        print(f"Removed todo: {removed_todo}")
    except IndexError:
        print("Invalid todo index.")
    except ValueError:
        print("Invalid input. Please enter the number of the todo to remove.")

def main():
    todos = []

    while True:
        print("\nTodo App Menu:")
        print("1. Add todo")
        print("2. List todos")
        print("3. Remove todo")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter todo task: ")
            add_todo(todos, task)
        elif choice == "2":
            list_todos(todos)
        elif choice == "3":
            list_todos(todos)
            index = input("Enter the number of the todo to remove: ")
            remove_todo(todos, index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()