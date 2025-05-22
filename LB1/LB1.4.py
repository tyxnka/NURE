tasks = {
    "Прибрати кімнату": "очікує",
    "Написати звіт": "в процесі",
    "Оплатити рахунки": "виконано"
}

def add_task(name, status="очікує"):
    if name not in tasks:
        tasks[name] = status
    else:
        print(f"Задача '{name}' вже існує.")

def remove_task(name):
    if name in tasks:
        del tasks[name]
    else:
        print(f"Задача '{name}' не знайдена.")

def update_status(name, new_status):
    if name in tasks:
        tasks[name] = new_status
    else:
        print(f"Задача '{name}' не знайдена.")

add_task("Купити продукти")
update_status("Написати звіт", "виконано")
remove_task("Оплатити рахунки")

waiting_tasks = [task for task, status in tasks.items() if status == "очікує"]

print("Поточні задачі:", tasks)
print("Задачі зі статусом 'очікує':", waiting_tasks)
