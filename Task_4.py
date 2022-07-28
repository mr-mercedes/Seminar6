# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


N = int(input("Введите N: "))

my_list = [int(i) for i in range(N + 1)]

f = lambda x: 3 * x + 1

for i in range(len(my_list)):
    my_list[i] = f(my_list[i])

my_list.remove(my_list[0])

print(dict(enumerate(my_list, 1)))
