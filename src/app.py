
# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from tasks import todo_list, create_task,delete_task,mark_as_finished,delete_all_tasks # import other functions as well
from accounts import accounts, add_account,login  # import the function as well


if __name__ == "__main__":
    """
     Allow a person to input a name and a password

        E.g

    """
 
    name = input("Enter your name: ")
    password=input("enter your password: ")

    login(password,name)

    while True:
        print('Select Options')
        print('1. creating a task')
        print('2. deleting a task ')
        print('3. deleting all tasks')
        print('4. Marking a task finished')
        choice=int(input('Selection: '))
        if choice == 1:
            create_task()
        elif choice == 2:
            onm=input('enter a task to delete\n')
            delete_task(onm)
        elif choice == 3:
            delete_all_tasks()
        elif choice == 4:
           task=input('enter task to mark as finished')
           mark_as_finished(task)
        else:
            print('Select Options')
            print('1. creating a task')
            print('2. deleting a task ')
            print('3. deleting all tasks')
            print('4. Marking a task finished')
            choice=int(input('Selection: '))
            if choice == 1:
                create_task()
            elif choice ==2:
                onm=input('enter a task to delete\n')
                delete_task(onm)
            elif choice == 3:
                delete_all_tasks()
            elif choice == 4:
                task=input('enter task to mark as finished')
                mark_as_finished(task)
            

   