# 2- Найти сумму чисел списка стоящих на нечетной позиции
# [1, 2, 3, 5, 1, 5, 3, 10]


from functools import reduce


my_nums = [1, 2, 3, 5, 1, 5, 3, 10]

result = reduce(lambda x, y: x + y, my_nums[1::2])
print(result)
