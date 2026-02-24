# 7. Todo List Manager (add, view, remove)

tasks = []

while True:
    print("\n1.Add Task 2.View Tasks 3.Remove Task 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif ch == "2":
        print("Tasks:")
        for i, t in enumerate(tasks, 1):
            print(i, t)

    elif ch == "3":
        num = int(input("Task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)

    elif ch == "4":
        break