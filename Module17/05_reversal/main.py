# TODO здесь писать код

line = input("Введите строку: ")
i_first = line.index("h")
i_last = -line[::-1].index("h") - 1
line_result = line[i_last - 1:i_first:-1]
print(
    "Развёрнутая последовательность между первым и последним h:", line_result
)
