import os

FILENAME = "tasks.txt"

def load_tasks():
    """Загружает задачи из файла."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Сохраняет задачи в файл."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")

def show_tasks(tasks):
    """Выводит список задач."""
    if not tasks:
        print("\n[!] Список задач пуст.")
    else:
        print("\n--- Ваши задачи ---")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Добавляет новую задачу."""
    task = input("Введите описание задачи: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f" Задача '{task}' добавлена!")

def remove_task(tasks):
    """Удаляет задачу по номеру."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Введите номер задачи для удаления: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f" Задача '{removed}' удалена.")
        else:
            print(" Неверный номер.")
    except ValueError:
        print(" Пожалуйста, введите число.")

def main():
    """Основной цикл программы."""
    tasks = load_tasks()
    print("Welcome to the Professional To-Do App!")
    
    while True:
        print("\n1. Добавить | 2. Показать | 3. Удалить | 4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print(" До свидания!")
            break
        else:
            print(" Неизвестная команда.")

if __name__ == "__main__":
    main()
        
