def menu():
	print("""
		1. Add a task
		2. view a task
		3. Mark a task as complete
		4. Delete a task
		5. Exit
		""")

def add_task(task):
        task = user_input
        return 

def view_all_task(view_a_task):
    if not to_do_manager:
        print("invalid input")
    return 
    

    for task in to_do_manager:
        for x in range(number):
            print(f"{x+1}{mark_box[x]} {task[x]}")
    
def mark_task_complete(mark_a_task_as_complete):
    if not to_do_manger:
        print("invalid input")
    return 
    
    for task in to_do_manger:
        print(f"{[x]} {task['task']}")

def delete(delete_a_task):
    "delete all"

def exit():
    print("existing the app.Goodbye")
    exist()

to_do_manager = []

def main():
	while True:
		menu()
		user_input = input("Enter a number: ")
		if user_input == "1":
			try:
				task = input("Enter the task: ")
		    except ValueError:
				    print("invalid input Gadus correct yourself")
				    print("Task added")
				    add_task(task)
		elif user_input == "2":
			view_task()
		elif user_input == "3":
			mark_task_complete()
		elif user_input == "4":
			delete()
		elif user_input == "5":
			exit()
		else:
			    print("Enter from 1 - 5")
			    
main()
						
				
				
					
			
	
