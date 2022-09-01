# TODO здесь писать код

familys = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Иванова", "Анастасия"): 30,
    ("Иванов", "Константин"): 19
}

surname = input("Введите фамилию: ").capitalize()
print("\n")

for names, age in familys.items():

    if surname[:-2] in names[0]:
        print(*names, age)
