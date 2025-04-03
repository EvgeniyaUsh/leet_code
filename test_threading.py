import threading
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in "abcde":
        print(letter)
        time.sleep(1)


# Создаем два потока
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# # Запускаем потоки
# thread1.start()
# thread2.start()

# # Ждем завершения обоих потоков
# thread1.join()
# thread2.join()

# print("Задачи завершены")


import threading

# Переменная для подсчета
counter = 0
counter_lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(100000):
        with counter_lock:  # Захватываем замок, чтобы только один поток изменял counter
            counter += 1


# Создаем два потока, которые увеличивают счетчик
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Задача {n} начала выполнение")
    time.sleep(1)
    print(f"Задача {n} завершена")
    return f"Результат задачи {n}"

# Создаем пул потоков
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))

# Выводим результаты выполнения задач
for result in results:
    print(result)

