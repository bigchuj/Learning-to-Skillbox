# TODO здесь писать код


def is_len_three(list_):

    return len(list_) == 3


def is_letter_name(name):

    return name.isalpha()


def is_email_name(email):

    return "." in email and "@" in email


def is_number(num):

    return (10 <= int(num) <= 99) and num.isalnum()


with open("registrations.txt", "r", encoding="utf-8") as reg:

    for line in reg:

        values = line.split()  # список из содержимого

        try:
            if not is_len_three(values):
                raise IndexError("НЕ присутствуют все три поля")

            elif not is_letter_name(values[0]):
                raise NameError("Поле «Имя» содержит НЕ только буквы")

            elif not is_email_name(values[1]):
                raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")

            elif not is_number(values[2]):
                raise ValueError(
                    "Поле «Возраст» НЕ является числом от 10 до 99")

        except (IndexError, NameError, SyntaxError, ValueError) as er:

            with open("registrations_bad.log", "a", encoding="utf-8") as reg_bad:

                reg_bad.write(
                    "{} - {}\n".format(' '.join(values).ljust(50), er))

        else:
            with open("registrations_good.log", "a", encoding="utf-8") as reg_good:
                reg_good.write(line)
