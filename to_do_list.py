import time

tasks = []

if __name__ == "__main__":
    print("Welcome to the To-Do List app: ")

    while True:
        print('\n')
        print("Please select one of the following options: ")
        print("----------------------")
        print("1. Add a task: ")
        print("2. Remove a task: ")
        print("3. List tasks: ")
        print("4. Quit: ")

        choice = input('Enter your choice: ')

        if choice == '1':

            break_variable = 1
            while True:

                if break_variable == 2:
                    break
                
                task = input('Enter a task: ')
                tasks.append(task)
                time.sleep(1)

                while True:

                    keep_going = input("Would you like to add another task: (y/n)")
                
                    if keep_going.lower() == 'y':
                        print("\n")
                        break

                    elif keep_going.lower() == 'n':
                        break_variable = 2
                        break

                    else:
                        print('Please enter a valid response: ')
                        continue

        elif choice == '2':
            print(tasks)
            task_to_remove = input('Enter the task to be removed: ')
            tasks.remove(task_to_remove)
            
            print(tasks)
            time.sleep(3)

        elif choice == '3':
            if tasks == []:
                
                print("\n")
                print('You have no current tasks: ')
                time.sleep(3)
            
            else:
                print(tasks)
                time.sleep(5)

        elif choice == '4':
            break

        else:
            print('Please choose a valid option: ')
            time.sleep(3)

    print(f"Your task list is: {tasks}")