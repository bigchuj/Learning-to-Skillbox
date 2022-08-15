# TODO здесь писать код

while True:
    password = input("Придумайте пароль: ")
    message_error = "Пароль ненадёжный. Попробуйте ещё раз."
    messege_done = "Это надёжный пароль!"

    if len(password) < 8:
        print(message_error)
        continue

    count_digit = 0
    letter_upper = 0
    for elem in password:
        count_digit += 1 if elem.isdigit() else 0
        letter_upper += 1 if elem.isupper() else 0

    if count_digit < 3 or not letter_upper:
        print(message_error)
        continue

    print(messege_done)
    break
