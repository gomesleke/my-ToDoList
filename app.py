#to do list
import os
import time
'''
add task - name | level |
look
mark 

'''

tasks= []

def add_task():
    task_input=input('Add a task: ')
    tasks.append(task_input)
    print(f'Task add: {task_input}',time.asctime())

print(tasks)
add_task()