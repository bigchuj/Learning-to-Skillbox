# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу

def remove_digit_from_list(my_list, digit):

    for _ in my_list:
        if digit in my_list:
            my_list.remove(digit)
        else:
            break


numbers = [1, 5, 3]
numbers_first = [1, 5, 1, 5]
numbers.extend(numbers_first)
num_count_5 = numbers.count(5)
remove_digit_from_list(numbers, 5)
numbers.extend([1, 3, 1, 5, 3, 3])
num_count_3 = numbers.count(3)

print("Результат работы программы:")
print("Кол-во цифр 5 при первом объединении:", num_count_5)
print("Кол-во цифр 3 при втором объединении:", num_count_3)
print("Итоговый список:", numbers)
