def main():
    tasks = [] #EmptyList

    while True:
        print(f"Tasks to do:{len(tasks)}")
        print(tasks)
        
        command = input("What do you want to do?(add, complete, exit):")
        if command == "add":
                new_task= input("Enter new task:")
                tasks.append(new_task)
        elif command == "complete":
             comp_task = input("Which task did you complete?")
             tasks.remove(comp_task)
        elif command == "prioritize":
             pri_task = input("What task do you want to prioritize? ")
             tasks.insert(0,pri_task)
        elif command == "exit":
             print("Byeee")
             break

if __name__=="__main__":
    main()
