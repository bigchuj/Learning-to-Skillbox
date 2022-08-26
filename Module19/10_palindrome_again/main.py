# TODO здесь писать код

def palindrome(word: str) -> None:

    words = set(word)
    results = {
        "pozitive": "Можно сделать палиндромом",
        "negative": "Нельзя сделать палиндромом"
    }

    if len(word) % 2:

        for letter in words:

            count = 0
            if count > 1:
                print(results["negative"])
                break

            elif word.count(letter) == 1:
                count += 1
        else:
            print(results["pozitive"])

    else:

        for letter in words:

            if word.count(letter) == 1:
                print(results["negative"])
                break

        else:
            print(results["pozitive"])


word = input("Введите строку: ")
palindrome(word)
