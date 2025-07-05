import json
import os

tasks = []

def save_tasks(filename="tasks.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def load_tasks(filename="tasks.json"):
    global tasks
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
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
    save_tasks()
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
            save_tasks()
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
            save_tasks()
            print("Задача удалена.")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Ошибка ввода. Введите номер задачи.")

# Загружаем задачи при запуске программы
load_tasks()

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
