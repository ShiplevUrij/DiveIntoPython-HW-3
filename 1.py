# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

my_list = [1, 1, 11, 2, 3, 3, 2, 1, 11, 5, 5, 8, 7, 11, 12]
new_list = []
my_set = set(my_list)

for item in my_set:
    if my_list.count(item) > 1:
        new_list.append(item)

print(new_list)