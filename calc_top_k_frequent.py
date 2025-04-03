"""
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

import heapq

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2


def top_k_frequent_heap(words, k):
    dw = {}
    for i in words:
        dw[i] = dw.get(i, 0) + 1

    heap = [(-count, world) for world, count in dw.items()]

    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]


result = top_k_frequent_heap(words, k)
print(result)


import sys

# n = int(sys.stdin.readline().strip())

# current_length = 0
# max_length = 0

# for _ in range(n):
#     num = int(sys.stdin.readline().strip())
#     if num == 1:
#         current_length += 1
#     else:
#         max_length = max(max_length, current_length)
#         current_length = 0

# max_length = max(max_length, current_length)


# n = int(sys.stdin.readline().strip())
# mass = []

# for _ in range(n):
#     num = int(sys.stdin.readline().strip())
#     if num not in mass:
#         mass.append(num)

# for i in mass:
#     print(i)

# n = int(sys.stdin.readline().strip())
# prev = None

# for _ in range(n):
#     num = int(sys.stdin.readline().strip())
#     if num != prev:
#         print(num)
#         prev = num


import sys

# Считываем число n
# n = int(sys.stdin.readline().strip())


# Рекурсивная функция для генерации скобочных последовательностей
def generate(current, open_count, close_count):
    # Если длина текущей строки достигла 2 * n, выводим её
    if len(current) == 2 * 3:
        print(current)
        return

    # Если открывающих скобок меньше n, добавляем ещё одну
    if open_count < 3:
        generate(current + "(", open_count + 1, close_count)

    # Если закрывающих скобок меньше, чем открывающих, добавляем )
    if close_count < open_count:
        generate(current + ")", open_count, close_count + 1)


# Запускаем генерацию с пустой строкой и нулями для скобок
generate("", 0, 0)


# Возвести в число в степень через рекурсию

# x2 = x*x
# xn = (x)(n-1)*x
# x0 = 1
# 0,1,1,2,3,5,8
# x3 = x2 + x1
# x4 = x3*x


# def fibb(x, n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return x
#     else:
#         return fibb(x, n - 1) * x


# a = fibb(2, 4)
# print(a)

# def foo(x, n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return x
#     else:
#         return foo(x, n - 1) * x


# dd = foo(3, 4)
# print(dd)
