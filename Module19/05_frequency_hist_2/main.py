# TODO здесь писать код

line = input("Введите текст: ")

frequency_elements_orig = dict()

for elem in line:

    if elem in frequency_elements_orig:
        frequency_elements_orig[elem] += 1
    else:
        frequency_elements_orig[elem] = 1


frequency_elements_inverted = dict()

for elem, quantity in frequency_elements_orig.items():

    if quantity in frequency_elements_inverted:
        frequency_elements_inverted[quantity].append(elem)
    else:
        frequency_elements_inverted[quantity] = [elem]


print("Оригинальный словарь частот:")
[
    print(f'{elem} : {quantity}')
    for elem, quantity in frequency_elements_orig.items()
]

print("\nИнвертированный словарь частот:")
[
    print(f'{elem} : {quantity}')
    for elem, quantity in frequency_elements_inverted.items()
]
