shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код

part = input("Название детали: ")
count_part = 0
summ_price = 0

for elem in shop:
    if part in elem:
        count_part += 1
        summ_price += elem[1]

print("Кол-во деталей —", count_part)
print("Общая стоимость —", summ_price)
