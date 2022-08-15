# TODO здесь писать код

ip_address = input("Введите IP: ").split(".")

for i in ip_address:

    if len(ip_address) < 4:
        print("Адрес — это четыре числа, разделённые точками.")
        break

    if not i.isdigit() and not int(i) < 0:
        print(f"{i} — это не целое число.")
        break

    elif int(i) > 255:
        print(f"{i} превышает 255")
        break

    elif int(i) < 0:
        print(f"{i} меньше 0")
        break

else:
    print("IP-адрес корректен.")
