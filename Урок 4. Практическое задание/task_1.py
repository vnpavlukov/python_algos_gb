"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit
# i will make oi later


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in nums if i % 2 == 0]


my_lst = [i for i in range(10000)]

print(timeit("func_1(my_lst)", globals=globals(), number=2000))  # 2.3062951000000003
print(timeit("func_2(my_lst)", globals=globals(), number=2000))  # 1.1134026000000001

'''
во втором случае быстрее в два раза
'''