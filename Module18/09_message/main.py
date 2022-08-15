# TODO здесь писать код

message = input("Сообщение: ")
result_message = []
temp_word = []

for elem in message:
    if elem.isalpha():
        temp_word.append(elem)
    else:
        temp_word.reverse()
        result_message.append(''.join(temp_word))
        temp_word.clear()
        result_message.append(elem)

print("Новое сообщение:", ''.join(result_message))
