tasks=[]

def add_task():
    task=input("\nEnter the task to add:")
    tasks.append(task)
    print("Task added successfully.")

def view_task():
    if not tasks:
        print("\nTask list is empty")
    else:
        print("\nYour Tasks:")
        for idx,task in enumerate(tasks,1):
            print(f"{idx}.{task}")
            
def delete_task():
    view_task()

    try:
        to_remove=int(input("\nEnter the task number to remove:"))

        remove=tasks.pop(to_remove - 1)
        print(f"\nTask : {remove} removed successfully.")

    except Exception as e:
        print("Invalid task number")

while True:
    print("\n---To Do List---\n")
    print("1.Add Tasks\n2.View Tasks\n3.Delete Tasks\n4.Exit")

    choice=int(input("Enter your choice:"))

    if(choice == 1):
        add_task()
    elif(choice==2):
        view_task()
    elif(choice==3):
        delete_task()
    elif(choice==4):
        print("Done")
        break
    else:
        print("Invalid choice!Enter a valid choice.")
