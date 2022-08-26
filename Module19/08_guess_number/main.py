# TODO здесь писать код

max_range_number = int(input("Введите максимальное число: "))

numbers_yes = set()
numbers_no = set()


while True:
    temp_value = input("\nНужное число есть среди вот этих чисел: ")

    if temp_value == "Помогите!":
        print("Артём мог загадать следующие числа:",
              *sorted(numbers_yes - numbers_no))
        break

    nums = set(temp_value.split())
    answer = input("Ответ Артёма: ").lower()

    if answer == "да":
        numbers_yes.update(nums)

    elif answer == "нет":
        numbers_no.update(nums)
