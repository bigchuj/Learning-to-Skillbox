violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код

number = int(input("Сколько песен выбрать? "))
count_minutes = 0

for i in range(number):

    song_title = input(f"Название {i + 1}-й песни: ")

    for song in violator_songs:
        if song_title in song:
            count_minutes += song[1]
            break

print("\nОбщее время звучания песен:", round(count_minutes, 2), "минуты")
