# Programmer: Sherry Zhang
# Date: 2/5/2025
# A functional to-do list application that can support add, delete, view tasks

# display a menu with options to add
def display_menu():
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Quit the application")

# Add a task
def add_task(task):
    item = input("Input the task you want to add: ")
    # Ensure the input is not empty
    while not item:
        print("Your input is invalid")
        item = input("Input the task you want to add: ")
    
    task.append(item)

    print(f"Updated task: {task}")
    return task

# Delete tasks from the current task list
def delete_task(task):
    # If not task
    if not task:
        print("No tasks to delete!")

    item = input("Input the task you want to delete: ")

    while item not in task:
        print("The task you want to delete does not exist!")
        item = input("Input the task you want to delete: ")
    
    task.remove(item)
    print(f"Updated task: {task}")
    return task

# Main Function
# Store task in a list
def main():
    # Store tasks into a list
    task = []

    # Welcome users
    print("Welcome to the to-do list application!")

    while True:
        # Display menu with options
        display_menu()
        option = input("Choose the option: ").strip()

        while (option not in ["1", "2", "3", "4"]):
            print("Your option is invlid!")
            option = input("Choose the option: ")

        if option == "1":
            task = add_task(task)
        elif option == "2":
            print(f"Task list: {task}")
        elif option == "3":
            task = delete_task(task)
        elif option == "4":
            print("Bye! Exiting the application")
            break


# Run the program
if __name__ == "__main__":
    main()
