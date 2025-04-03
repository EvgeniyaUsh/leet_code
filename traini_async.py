import asyncio
from asyncio import sleep


async def make_request():
    await sleep(0.1)
    return 1


# async def main():
#     chunk = 100
#     count = 0
#     tasks = []

#     for i in range(10_000):
#         count += 1
#         tasks.append(asyncio.create_task(make_request()))
#         if len(tasks) == chunk or count == 10_000:
#             res = await asyncio.gather(*tasks)
#             print(res)
#             tasks = []
#             print(count)


# asyncio.run(main())

# import os
# from time import sleep


# import asyncio
# import random


# async def worker(semaphore):
#     async with semaphore:  # 🔹 Блокируем выполнение, если лимит исчерпан
#         print(f"Задача запущена")
#         await asyncio.sleep(random.uniform(1, 3))  # Симуляция работы
#         print(f"Задача завершена")


# async def main():
#     semaphore = asyncio.Semaphore(4)  # Разрешаем максимум 3 задачи одновременно
#     tasks = [worker(semaphore) for i in range(10)]
#     await asyncio.gather(*tasks)  # Запускаем все задачи


# asyncio.run(main())


# import asyncio
# import random

# Создаем семафор с лимитом на 3 одновременные задачи
# semaphore = asyncio.Semaphore(3)


# async def limited_task(task_id):
#     # Ждём разрешения от семафора
#     async with semaphore:
#         print(f"Начало задачи {task_id}")
#         # Эмуляция работы (например, запрос к API)
#         await asyncio.sleep(random.uniform(1, 3))
#         print(f"Завершение задачи {task_id}")


# async def main():
#     # Создаем и запускаем 10 задач
#     tasks = [limited_task(i) for i in range(10)]
#     await asyncio.gather(*tasks)


# # Запускаем event loop
# asyncio.run(main())


async def nested():
    return 42


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    s = await task
    raise TimeoutError


asyncio.run(main())
