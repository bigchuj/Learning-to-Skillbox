# TODO здесь писать код

first_students = list(range(160, 177, 2))
second_students = list(range(162, 181, 3))
first_students.extend(second_students)
first_students.sort()  # есть же метод сортировки

print("Отсортированный список учеников:", first_students)