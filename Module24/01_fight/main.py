# TODO здесь писать код

from random import choice


class Fighters:

    def __init__(self,
                 fighter_1=None,
                 fighter_2=None,
                 health_fighter=100,
                 data_fighters={
                     "Убит": [],
                     "Fighers": {}
                 }
                 ) -> None:

        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.health_fighter = health_fighter
        self.data_fighters = data_fighters

    # регистрация юнитов

    def registration_fighter(self):

        while (
            self.fighter_1 in self.data_fighters["Fighers"] or
            self.fighter_1 in self.data_fighters["Убит"]
        ):

            print("Юнит с данным именем уже был зарегистрирован.\n")
            self.fighter_1 = input("Пожалуйста введите другое имя: ")

        else:
            self.data_fighters["Fighers"].update(
                {self.fighter_1: self.health_fighter}
            )
            return True

    # регистрируем повреждения юнитов или убитых юнитов

    def damage(self):

        self.data_fighters["Fighers"][self.fighter_2] -= 20

        if self.data_fighters["Fighers"][self.fighter_2] > 0:

            print(
                "{fighter_2} атаковал {fighter_1}\nУ {fighter_1} осталось здоровья - {health_1}".format(
                    fighter_2=self.fighter_2,
                    fighter_1=self.fighter_1,
                    health_1=self.data_fighters["Fighers"][self.fighter_2]
                )
            )

        else:
            print(
                "{fighter_2} атаковал {fighter_1}\n{fighter_1} - убит.".format(
                    fighter_2=self.fighter_2,
                    fighter_1=self.fighter_1
                )
            )
            del self.data_fighters["Fighers"][self.fighter_2]
            self.data_fighters["Убит"].append(self.fighter_2)

   # метод возвращает требуемое значение из базы данных юнитов

    def fighters(self, key):
        return self.data_fighters[key]


class Aktivity:

    # здесь мы атакуем случайными юнитами

    def attack(self):

        fighters = Fighters().fighters("Fighers")
        len_fighters = len(fighters)
        option = input(
            "Нажмите Enter для атаки. Для выхода введите любой символ + Enter. "
        )

        if len_fighters > 1 and not option:

            fighter_1 = choice(list(fighters))
            fighter_2 = choice(list(fighters))

            while fighter_2 == fighter_1:

                fighter_1 = choice(list(fighters))
                fighter_2 = choice(list(fighters))

            damage = Fighters(fighter_1, fighter_2)
            damage.damage()

            return True

        else:
            # если у нас один игрок, то программа требует зарегистрировать еще одного
            # однако, если option указано любое значение и при этом один юнит,
            # то программа прекратит выполнение
            if not option:
                print(
                    "Вы можете проводить атаку двумя игроками. Зарегистрируйте еще одного."
                )

                return Aktivity().registration()

            else:
                return False

    # регистрация юнитов

    def registration(self):

        name_fighter = input(
            "Введите имя юнита или нажмите Enter для начала атак: "
        )

        if name_fighter:

            reg_fighter = Fighters(fighter_1=name_fighter)
            return reg_fighter.registration_fighter()

        else:
            return False

    # приветствие перед началом игры

    def welcome(self):
        print(
            'Добро пожаловать в нашу игру "Драка".\nДля начала зарегистрируйте юнитов'
        )

    # итоги игры

    def result_game(self):

        fighters_1 = Fighters().fighters("Fighers")
        fighters_2 = Fighters().fighters("Убит")
        
        print("Оставшиеся юниты:")
        [print(
            "Юнит: {}, осталось очков: {}".format(name, score)
        ) for name, score in sorted(fighters_1.items())]

        print("\nУбитые юниты:")
        [print(name) for name in sorted(fighters_2)]


welc = Aktivity().welcome()

reg_fighter = Aktivity()
while reg_fighter.registration():
    pass

print("Теперь можете приступать к совершению атак.")

attack = Aktivity()
while attack.attack():
    pass

else:  # возможно можно без данного блока
    print("Спасибо за игру, результат:\n")
    result = Aktivity()
    result.result_game()
