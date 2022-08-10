# TODO здесь писать код

# количество друзей:
quattity_frends = [0 for _ in range(int(input("Кол-во друзей: ")))]
debentures = int(input("Долговых расписок: "))

for i in range(debentures):
    print(f"\n{i + 1}-я расписка")
    index_input = int(input("Кому: ")) - 1
    index_output = int(input("От кого: ")) - 1
    total = int(input("Сколько: "))
    quattity_frends[index_input] -= total
    quattity_frends[index_output] += total

print("\nБаланс друзей:")
for i, balance_ in enumerate(quattity_frends):
    print(f"{i + 1}: {balance_}")