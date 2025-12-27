#to do list
import os
import time
'''
adicionar tasks -> nome | data | dificulade
visual
cortar
points

'''

tasks= []

def start():
    print('|| TO DO LIST ||\n')
    print('1 - Add task')
    print('2 - look list')
    print('3 - finish task')
    print('4 - points')
    print('5 - Exit')

def add_task():
    os.system('cls')
    task_input=input('Add a task: ')
    tasks.append(task_input)
    print(f'Task add: [ ] {task_input}|{time.asctime()}')
    time.sleep(5)
    back_to_menu()
    

def look():
    for task in tasks:
        print(f'[ ] {task}')

def cut_task():
    pass

def exit():
    print('Thanks...')
    print('Finish...')

def back_to_menu():
    input('Press any keyboard: ')
    main()


def invalid():
    print('Try again\n')
    back_to_menu()


def choice_options():
    choice=int(input('Choice a Number: '))
    try: 
        match choice:
            case 1:
                add_task()
            case 2:
                look()
            
            case 3:
                pass

            case 4:
                pass
            

            case 5:
                exit()
    except:
        invalid()


def main():
    start()
    choice_options()

    

if __name__=='__main__':
    main()
    