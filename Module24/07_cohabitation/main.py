# TODO здесь писать код

from random import randint


class Human:
    def __init__(self, name) -> None:
        self.name = name
        self.satiety = 50

    def to_eat(self):
        self.satiety += 5
        Home.refrigerator_with_food -= 10

    def to_work(self):
        self.satiety -= 10
        Home.bedside_table_with_money += 40

    def to_play(self):
        self.satiety -= 10

    def go_to_market(self):
        Home.refrigerator_with_food += 30
        Home.bedside_table_with_money -= 50


class Home:
    refrigerator_with_food = 50
    bedside_table_with_money = 0


def write_to_report(text="", indention=0):
    with open("report.txt", "a", encoding="utf-8") as report:
        report.write(" " * indention + text + "\n")


people = [Human("Человек " + str(i_name + 1)) for i_name in range(2)]
count_day = 0

while count_day < 366:
    count_day += 1
    write_to_report(f"\nДень {count_day}")
    write_to_report(
        f"В холодильнике {Home.refrigerator_with_food} еды, а в тумбочке {Home.bedside_table_with_money} денег.", 2)

    for human in people:
        number = randint(1, 6)
        write_to_report()
        write_to_report(f"На кубике выпала цифра: {number}", 2)
        write_to_report(f"{human.name}, {human.satiety} пунктов здоровья", 2)

        if human.satiety <= 0:
            write_to_report("Умер, потому что не хватило еды((", 4)
            del people[people.index(human)]
        elif (human.satiety < 20 or number == 2) and Home.refrigerator_with_food > 0:
            write_to_report("Покушал", 4)
            human.to_eat()
        elif Home.refrigerator_with_food < 10 and Home.bedside_table_with_money >= 50:
            write_to_report("Сходил в магазин", 4)
            human.go_to_market()
        elif Home.bedside_table_with_money < 50 or number == 1:
            write_to_report("Ушел поработать", 4)
            human.to_work()
        else:
            write_to_report("Играет", 4)
            human.to_play()

    write_to_report()

    if not people:
        break

else:
    write_to_report(
        f"На конец года в холодильнике {Home.refrigerator_with_food} еды, а в тумбочке {Home.bedside_table_with_money} денег.\n")
