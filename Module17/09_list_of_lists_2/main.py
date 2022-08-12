nice_list = [
    [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ],
    [
        [10, 11, 12], [13, 14, 15], [16, 17, 18]
    ]
]

# TODO здесь писать код

results = [
    elem for elements_1 in nice_list for elements_2 in elements_1 for elem in elements_2
]

print("Ответ:", results)
