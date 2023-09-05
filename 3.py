# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав 
# его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

MAX_WEIGTH = 5_000
things = ['Ложка', 'Кружка', 'Тарелка', 'Нож', 'Палатка', 'Футболка',
          'Брюки', 'Кофта', 'Спальный_мешок', 'Одеяло']
weights = [50, 250, 300, 150, 3_500, 300, 400, 480, 770, 1_670]

my_dict = {}
for num, thing in enumerate(things):
    my_dict[thing] = weights[num]

weight = 0
things_in = []
for key, value in my_dict.items():
    weight += value
    if weight <= MAX_WEIGTH:
        things_in.append(key)
    else:
        weight -= value
print(things_in)