# TODO здесь писать код

from random import uniform

team_1 = [round(uniform(5.0, 10.0), 2) for _ in range(20)]
team_2 = [round(uniform(5.0, 10.0), 2) for _ in range(20)]

team_winners = [
    (elem_1 if elem_1 > elem_2 else elem_2)
    for elem_1, elem_2 in zip(team_1, team_2)
]

print("Первая команда:", team_1)
print("Вторая команда:", team_2)
print("Победители тура:", team_winners)
