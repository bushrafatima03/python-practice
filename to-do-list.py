tasks = []
task = input("Enter a task:")
tasks.append(task)
while True:
    task = input("Enter a task:")
    if task == "done":
        break
    tasks.append(task)
print("\nYour To-do List:")
for i,task in enumerate(tasks,start=1):
    print(i,"-",task)
remove = input("Enter the task number to remove:")
remove = int(remove)
if remove <= len(tasks):
     tasks.pop(remove - 1)
     print("Task removed!")
else:
     print("Invalid task number.")