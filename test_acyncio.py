import asyncio


async def task_1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")


async def task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")


# async def main():
#     await asyncio.gather(task_1(), task_2())


# asyncio.run(main())

lock = asyncio.Lock()


async def critical_section(task_id):
    async with lock:
        print(f"Task {task_id} is working in the critical section")
        await asyncio.sleep(5)
        print(f"Task {task_id} finished working in the critical section")


# async def main():
#     await asyncio.gather(critical_section(1), critical_section(2))


# asyncio.run(main())


async def task_1():
    await asyncio.sleep(3)
    return "Result 1"


async def task_2():
    await asyncio.sleep(2)
    return "Result 2"


async def main():
    done, pending = await asyncio.wait(
        [asyncio.create_task(task_1()), asyncio.create_task(task_2())],
        return_when=asyncio.ALL_COMPLETED,
    )

    # done - это множество завершённых задач
    for task in done:
        print(f"Task completed with result: {task.result()}")  # Получаем результат
        print(repr(task_2))


async def main():
    # tasks = [asyncio.create_task(task_1()), asyncio.create_task(task_2())]
    try:
        result = await asyncio.wait_for(task_1(), timeout=3)  # Таймаут 2.5 секунды
        print(result)
    except TimeoutError:
        pass


# import aiofiles


# async def write_text(filename, text):
#     async with aiofiles.open(filename, mode="w") as file:
#         await file.write(text)


# async def main():
#     await asyncio.gather(write_text("file.txt", "text"), write_text("file1.txt", "text1"))


# asyncio.run(main())

# import aiohttp
# import asyncio


# async def fetch(url, max_ret):
#     async with aiohttp.ClientSession() as session:
#         async with session.head(url) as response:
#             status = response.status
#             if status == 200:
#                 res = await response.text()
#                 print(res)
#             print(f"Fetched {url} with status code {status}")


# async def main():
#     urls = ["https://example.com", "https://google.com", "https://translate.google.com/"]
#     await asyncio.gather(*[fetch(url) for url in urls])


# asyncio.run(main())


import asyncio
import random


async def unreliable_task():
    random_num = random.random()
    if random_num < 0.7:
        print(random_num)
        raise Exception("Random failure")
    return "Success"


async def retry_task(max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            result = await unreliable_task()
            print(f"Task succeeded: {result}")
            return result
        except Exception as e:
            retries += 1
            wait_time = 2**retries  # Exponential backoff
            print(f"Attempt {retries} failed: {e}. Retrying in {wait_time} seconds...")
            await asyncio.sleep(wait_time)
    print("Max retries reached")


async def main():
    await retry_task()


# asyncio.run(main())


from functools import wraps


def param_for_cache_decorator(param):
    def cache_decorator(func):
        cache_dict = {}

        def inner(*args, **kwargs):
            key = args, tuple(kwargs)
            cache_dict_len = len(cache_dict)
            if key in cache_dict:
                print("используется кэш")
                return cache_dict[key]
            result = func(*args, **kwargs)
            if cache_dict_len < param:
                cache_dict[key] = result
            print("не используется кэш")
            return result

        return inner

    return cache_decorator


@param_for_cache_decorator(1)
def slow_function(a, b):
    print(f"Выполнение функции с аргументами {a} и {b}")
    return a + b


def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    value


class MyClass:
    def __new__(cls, *args):
        print("qqqqqqqqqqqq")

    def __init__(self, x):
        self.data = []
        print("asdasdasdas")

    def add_data(self, data):
        self.data.append(data)


# Создаем два объекта, которые ссылаются друг на друга
# a = MyClass(1)

d = {}

def func(*args, **kwargs):
    # print(args)
    # print(tuple(kwargs.items()))
    key = args, tuple(kwargs.items())
    print(key)
    if key in d:
        return d[key]
    d[key] = 2



f = func(1, 2, keys=1)
f = func(1, 2, keys=2)
print(f)
