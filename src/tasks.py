
# This file contains code that manages your todo_list

todo_list = []

# Write a function creates a task


def create_task():#something missing here
    """
    Adds the task (string value) to todo_list
    """

    for i in range(5):
        todo_list.append(input('Add a new task\n'))
    print(todo_list)
    return todo_list
        


def delete_task():
    """
    Removes the specified task 
    new= input('enter task to deletfrom the todo_list
    """
    for i in todo_list:
        if i== new:
            updated_list= todo_list.remove(i)
            return (updated_list)
            
        else:
            return todo_list
        


def mark_as_finished():
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    for i in range(len(todo_list)):
        labelled_list = todo_list[i] + '[finished]'
    return labelled_list





def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    empty_list=todo_list.clear()
    
    return empty_list

