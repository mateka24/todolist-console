tasks = []

def show_menu():
    print("\nМеню:")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("0. Выйти")

def add_task():
    title = input("Введите задачу: ")
    tasks.append({"title": title, "done": False})
    print("Задача добавлена.")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def mark_done():
    show_tasks()
    try:
        idx = int(input("Введите номер выполненной задачи: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Задача отмечена как выполненная.")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Ошибка ввода. Введите номер задачи.")

def delete_task():
    show_tasks()
    try:
        idx = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("Задача удалена.")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Ошибка ввода. Введите номер задачи.")

while True:
    show_menu()
    choice = input("Выберите опцию: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Некорректная опция.")
