# TODO здесь писать код


family = dict()
number = int(input('Введите количество человек: '))
for i in range(1, number):
    child_name, parent_name = input(f'{i} пара: ').split()
    if parent_name not in family:
        family[parent_name] = 0
    if child_name not in family:
        family[child_name] = family[parent_name] + 1

print('“Высота” каждого члена семьи:')
list_keys = list(family.keys())
list_keys.sort()
for i in list_keys:
    print(i, family.get(i))
