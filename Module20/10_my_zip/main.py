# TODO здесь писать код

def func_zip(obj_1, obj_2):

    len_iter = min(len(obj_1), len(obj_2))
    return ((obj_1[i], obj_2[i]) for i in range(len_iter))


line = "abcd"
nums = (10, 20, 30, 40)
gen = func_zip(line, nums)

print("""Строка: {}
Кортеж чисел: {}

Результат:
{}""".format(line, nums, gen)
)

[print(*gen, sep="\n")]
