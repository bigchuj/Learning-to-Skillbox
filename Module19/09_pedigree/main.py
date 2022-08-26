# TODO здесь писать код


def func(dict_, elem_1, elem_2, level_dict: dict, lev):

    if elem_2 in dict_:
        # если в ключах есть родитель, то потомка добавляем в список
        # базовый случай 1
        dict_[elem_2].append(elem_1)
        level_dict[elem_2] = lev
        level_dict[elem_1] = lev + 1
        return

    else:
        # если в ключах нет родителя, то перебираем значения словаря
        for value in dict_.values():
            lev += 1

            for elem in value:  # перебираем элементы списка

                if elem == elem_2:
                    # если элемент равен родителю, то меняем элемент списка value на
                    # словарь "родитель - потомок", базовый случай 2
                    i_elem = value.index(elem)
                    value[i_elem] = {elem_2: [elem_1]}
                    level_dict[elem_1] = lev + 1
                    return

                elif type(elem) == dict:
                    # если элемент - словарь, то работаем с ним в рекурсии
                    # пока не получим один из базовых случаев
                    func(elem, elem_1, elem_2, level_dict, lev)


numbers = {
    0: "Первая", 1: "Вторая",
    2: "Третья", 3: "Четвертая",
    4: "Пятая", 5: "Шестая",
    6: "Седьмая", 7: "Восьмая",
    8: "Девятая", 9: "Десятая"
}
quantity_peoples = int(input("Введите количество человек: "))

# test_list = [
#     ['Alexei', 'Peter_I'], ['Anna', 'Peter_I'],
#     ['Elizabeth', 'Peter_I'], ['Peter_II', 'Alexei'],
#     ['Peter_III', 'Anna'], ['Paul_I', 'Peter_III'],
#     ['Alexander_I', 'Paul_I'], ['Nicholaus_I', 'Paul_I']
# ]

lineage = dict()  # здесь хранится родословная
levels = dict()  # здесь хранятся уровни родословной
level = 0  # уровень родословной

# for couple in test_list:
for i in range(quantity_peoples - 1):
    couple = input(f"{numbers[i]} пара: ").split()

    if not lineage:
        # если словарь пуст, то добавляем родителя - потомка
        # потомок - список, потому как может быть несколько потомков
        lineage[couple[1]] = [couple[0]]
        # добавляем уровни родословной
        levels[couple[1]] = level
        levels[couple[0]] = level + 1

    else:
        # функция добавляет в словари родословную и уровни
        func(lineage, couple[0], couple[1], levels, level)


print("\n«Высота» каждого члена семьи:")
[print(*i) for i in sorted(levels.items())]
