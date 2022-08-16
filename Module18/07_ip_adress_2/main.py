# TODO здесь писать код

ip_address = input("Введите IP: ").split(".")

for i in ip_address:

    if len(ip_address) < 4:
        print("Адрес — это четыре числа, разделённые точками.")
        break

    if not i.isdigit():
        print(f"{i} — это не целое число.")
        break

    elif int(i) > 255:
        print(f"{i} превышает 255.")
        break

else:
    print("IP-адрес корректен.")
