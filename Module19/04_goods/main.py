goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код

result = dict()

for product in goods.keys():
    temp_product = store[goods[product]]
    temp_total_quantity = 0
    temp_sum_price = 0

    for values in temp_product:
        temp_total_quantity += values['quantity']
        temp_sum_price += (values['quantity'] * values['price'])

    result[product] = [temp_total_quantity, temp_sum_price]


[
    print('{0} - {1} {2}, стоимость {3:_d} {4}'
          .format(
              i, result[i][0],
              (
                  'штука' if result[i][0] % 10 == 1 else
                  ('штуки' if result[i][0] % 10 in [2, 3, 4] else 'штук')
              ),
              result[i][1],
              (
                  'рубль' if result[i][1] % 10 == 1 and not result[i][1] % 100 == 11 else
                  ('рубля' if result[i][1] % 10 in [2, 3, 4] and result[i][1] % 100 not in [
                   12, 13, 14, 15, 16, 17, 18, 19, 20] else 'рублей')
              )
          )
          .replace('_', ' '))  # как еще можно разбить на разряды?
    for i in result.keys()
]

# вообще, конструкция выше по мне так громоздкая получилась и все в print-е
# правильнее наверное было бы поместить все в отдельные переменные и потом
# через метод format вывести красиво print
# у меня возникает вопрос - что будет правильнее и эффективнее?
# и наверное лучше для написания красивого кода?
