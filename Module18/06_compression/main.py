# TODO здесь писать код

line = input("Введите строку: ")
temp_elem = ""
count_elem = 0
result = []

for elem in line:

    if not temp_elem:
        temp_elem = elem
        count_elem += 1
    elif elem == temp_elem:
        count_elem += 1
    else:
        result.append(temp_elem + str(count_elem))
        temp_elem = elem
        count_elem = 1

result.append(temp_elem + str(count_elem))
print("Закодированная строка:", ''.join(result))
