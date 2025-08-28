# to-do app

# credits: anugya mehrotra @ https://github.com/anugyamehrotra

print("")
print("")
print("")
print("    To-Do App  ")
print("-----------------")

taskBoard=[]

while True:
    print("\n---- To-Do List ----")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    print("\n")

    taskCreate = input("Enter your choice: ")

    # task management
    if taskCreate == '1':
        print("")
        try:
            
            noOfTask = int(input("Please enter how many tasks you would like to add: "))
            if noOfTask < 1:
                print("Number of tasks must be at least 1.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
            
        for i in range(noOfTask):
            newTask = input("Enter your task: ")
            newTaskTime = input("Enter a time or deadline for your task: ")

            taskBoard.append({"Task": newTask, "Time": newTaskTime, "done": False})
            print("Task added: " + newTask)

    # task view board
    elif taskCreate == '2':
        print("\n---- To-Do List - Current Tasks ----")
        if taskBoard == False:
            print("No tasks pending.")
        else:
            i = 1
            for notedTask in taskBoard:
                if notedTask["done"]:
                    taskCompletion = "done"
                else:
                    taskCompletion = "Not Done"
                if notedTask.get("Time"):
                    timeDateRelative = " (Time: " + notedTask["Time"] + ")"
                else:
                    timeDateRelative = ""
                print(str(i) + ". " + notedTask["Task"] + timeDateRelative + " - " + taskCompletion)
                i = i + 1
        input("\nPress Enter to exit the task board.")

    # task pending
    elif taskCreate == '3':
        if not taskBoard:
            print("No tasks to mark as done.")
            continue
        print("\n---- Mark Task as Done ----")

        i = 1
        for task in taskBoard:
            if notedTask["done"]:
                taskCompletion = "done"
            else:
                taskCompletion = "Not Done"
            print(str(i) + ". " + notedTask["Task"] + " - " + taskCompletion)
            i = i + 1

        try:
            choice = int(input("Enter the task number to mark as done: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        checkForCompletedTask = False
        i = 1
        for notedTask in taskBoard:
            if i == choice:
                task["done"] = True
                print("Task " + str(choice) + " marked as done: " + task["Task"])
                checkForCompletedTask = True
                break
            i = i + 1
            # credits: anugya mehrotra @ https://github.com/anugyamehrotra
        if not checkForCompletedTask:
            print("Invalid task number.")

    # task exit
    elif taskCreate == '4' or taskCreate.lower() in ('q', 'exit'):
        print("Exiting To-Do App. \n By @ https://github.com/anugyamehrotra")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")



print("""                                                                 
                                                                        
                           ▓▓▓▓▓                    ▓▓▓                 
       ▓▓▓▓▓▓            ▓▓▓   ▓▓▓               ▓▓▓▓▓▓▓▓               
      ▓▓▓  ▓▓▓           ▓▓     ▓▓               ▓▓    ▓▓▓              
     ▓▓▓    ▓▓            ▓▓▓▓▓▓▓                ▓▓▓   ▓▓▒              
      ▓▓▓ ░▓▓▓              ▓▓▓                   ▓▓▓▓▓▓                
        ▓▓▓▓                ▓▓▓        ▓▓░          ▓▓▓    ▓▓▓▓▓▓▓      
        ▓▓▓▓                ▓▓▓     ▓▓▓▓▓▓▓▓        ▓▓▓   ▓▓    ▓▓▓     
        ▓▓▓▒                ▓▓▓     ▓▓    ▓▓▓       ▓▓▓   ▓▓▒   ▓▓▓     
        ▓▓▓▒     ▓▓▓▓▓      ▓▓▓     ▓▓▓   ▓▓▓       ▓▓▓    ▓▓▓▓▓▓▓      
        ▓▓▓▒   ▓▓▓  ▓▓▓     ▓▓▓      ▓▓▓▓▓▓         ▓▓▓      ▓▓▓        
        ▓▓▓▒   ▓▓    ▒▓▓    ▓▓▓        ▓▓▒          ▓▓▓      ▓▓▓        
        ▓▓▓▓   ▓▓▓  ▓▓▓     ▓▓▓        ▓▓▒          ▓▓▓      ▓▓▓        
        ░▓▓▓     ▓▓▓▓▓      ▓▓▓        ▓▓▒          ▓▓▓      ▓▓▓        
        ░▓▓▓▓▓    ▓▓▓       ▓▓▓        ▓▓▒          ▓▓▓      ▓▓▓        
           ▓▓▓▓▓  ▓▓▓       ▓▓▓        ▓▓▒          ▓▓▓   ░▓▓▓▓         
              ▓▓▓▓▓▓▓       ▓▓▓        ▓▓▒          ▓▓▓ ▓▓▓▓▓           
                 ▓▓▓▓      ▓▓▓▓       ▓▓▓           ▓▓▓▓▓▓▓             
                  ▓▓▓     ▓▓▓▓       ▓▓▓            ▓▓▓▓▓               
                  ▓▓▓    ▓▓▓▓       ▓▓▓             ▓▓▓                 
                  ▓▓▓    ▓▓▓      ░▓▓░              ▓▓▓                 
                                                                        
            ▓▓▓▓  ▓▓▓    ▓▓▓    ▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓▓▓          
        ▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓   ▓▓▓ ▓▓▓  ▓▓▓▒        ▓▓▓▓▓▓▓             
          ▓▓▓▓▓   ▓▓▓    ▓▓▓  ▓▓▓▓▓▓▓▓▓  ▓▓▓   ▓▓▓  ▓▓▓▓ ▓▓▓▓           
               ▒  ▓▓▓    ▓▓▓ ▓▓▓      ▓▓▓  ▓▓▓▓▓    ▓▓▓    ▓▓▓▓         
                                                                        
         ▓▓▓▓▓▓▓   ▓▓▓      ▓▓▓   ▓▓▓ ▓▓▓▓▓▓▓▓▓▓    ▓▓  ▓▓▓             
        ▓▓▓        ▓▓▓      ▓▓▓   ▓▓▓ ▓▓▓▒   ▓▓▓   ▓▓      ▓▓▓▓▓        
        ▓▓▓   ▓▓▓▓ ▓▓▓      ▓▓▓   ▓▓▓ ▓▓▓▒   ▓▓▓▓  ▓      ▓▓▓▓▓         
         ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓░    ▓▓              
                                                                        
        ▓     ▓    ▓    ▓   ▓      ▓▓    ▓    ▓     ▓     ▓    ▓                                                                      
""")

# reference
    # credits: anugya mehrotra @ https://github.com/anugyamehrotra
    # - https://pub.aimind.so/creating-a-simple-to-do-list-in-python-c0f52ab15814
    # - https://www.w3schools.com/python/python_ref_functions.asp