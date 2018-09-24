
# This file contains code that manages your todo_list

todo_list = []

# Write a function creates a task


def create_task():#something missing here
    """
    Adds the task (string value) to todo_list
    """

    #for i in range(5):
    todo_list.append(input('Add a new task\n'))
    print(todo_list)
    return #todo_list
        

"""
def delete_task():
    
    Removes the specified task 
    
"""
'''
    ............................................................
    task_to_delete = input('enter task to deletfrom the todo_list\n')
    for i in todo_list:
        if  i is task_to_delete:
            books=todo_list.remove(task_to_delete)
            print(books)
        # else:
        #     print('task not in the list')
        #     return todo_list
       ..........................................................
'''
# def delete_task(onm):
    
#     for i in todo_list:
#         if i is onm:
#             todo_list.remove(onm)
#     print(todo_list)
#     return todo_list
def delete_task(onm):
    if onm in todo_list:
        todo_list.remove(onm)
    print(todo_list)
    return todo_list

def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    for i in range(len(todo_list)):
        if todo_list[i] == task:
            todo_list[i] += '[finished]'
        else:

            print("Task not found in list")
    print(todo_list)
    return todo_list
    # count=0
    # while count <= len(todo_list):
        
    #     if task in todo_list:
    #         todo_list[count]+= '[finished]'
    #         print(todo_list)

    #     count+=1
    
        
    
    # return todo_list




def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    todo_list.clear()
    print(todo_list)
    
    return todo_list
