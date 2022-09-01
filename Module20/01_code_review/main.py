students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# TODO исправить код


def interestings_and_len_surnames(dict_):

    interestigs = set()
    total_len_surnames = 0

    for student in students.values():
        interestigs.update(student['interests'])
        total_len_surnames += len(student['surname'])

    return interestigs, total_len_surnames


pairs = []
for i in students:
    pairs.append((i, students[i]['age']))

interestings, len_surnames = interestings_and_len_surnames(students)

print("Список пар \"ID студента — возраст\":", pairs)
print("Полный список интересов всех студентов:", interestings)
print("Общая длина всех фамилий студентов:", len_surnames)
