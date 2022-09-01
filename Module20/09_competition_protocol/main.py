# TODO здесь писать код

# test = [
#     [69485, "Jack", 1],
#     [95715, "qwerty", 2],
#     [95715, "Alex", 3],
#     [83647, "M", 4],
#     [197128, "qwerty", 5],
#     [95715, "Jack", 6],
#     [93289, "Alex", 7],
#     [95715, "Alex", 8],
#     [95715, "M", 9]
# ]

quantity_rec = int(input("Сколько записей вносится в протокол? "))

players = dict()

print("Записи (результат и имя):")

# for i in test: # for testing
for i in range(1, quantity_rec + 1):

    result, name = input(f"{i}-я запись: ").split()
    players[name] = [int(result), i]
    # players[i[1]] = [i[0], i[2]]  # for testing

print("Итоги соревнований:")

results_score = dict()
for name, result_items in players.items():

    res, rec = result_items

    if results_score.get(res):
        results_score[res].append((rec, name))

    else:
        results_score[res] = [(rec, name)]

results_list = []
for res in sorted(results_score.keys(), reverse=True):

    for rec, name in sorted(results_score[res]):
        results_list.append((name, res))  # , rec))  # rec for testing

for i in range(3):
    print("{0}-е место. {1} ({2})".format(i + 1, *results_list[i]))

# вывод результата в ТЗ некорректен, Jack достигает раньше своих очков чем Alex
# даже если на блокноте расписывать время получения очков, получим другой результат
