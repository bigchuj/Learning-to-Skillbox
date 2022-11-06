# TODO здесь писать код

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count_potato, count_potato_bed):
        # сделали количество грядок и количетсво картофеля на грядке
        self.potatoes = {
            key: [
                Potato(index) for index in range(1, count_potato + 1)
            ] for key in range(1, count_potato_bed + 1)
        }

    def grow_all(self, num_potato_bed):
        # передаем агрумент - номер грядки, за которой будет ухаживать садовник
        try:
            if self.potatoes[num_potato_bed]:
                for potato in self.potatoes[num_potato_bed]:
                    potato.grow()
                print('Картошка прорастает!')
                return True
            else:
                return self.are_all_ripe(num_potato_bed)

        except KeyError:
            error_num_garden_bed()

    def are_all_ripe(self, num_potato_bed_for_control):
        try:
            if not self.potatoes[num_potato_bed_for_control]:

                print("Грядка пустая, посадите на ней картошку.")
                option = input(
                    'Посадить картошку? "да" - любой символ, "нет" - нажать "Enter": ')

                if option:
                    self.potatoes[num_potato_bed_for_control] = [
                        Potato(index) for index in range(1, count_potato + 1)
                    ]
                else:
                    return False

            for potato in self.potatoes[num_potato_bed_for_control]:
                if not potato.is_ripe():
                    print('Картошка ещё не созрела!\n')
                    return False 
            else:
                print('Вся картошка созрела. Можно собирать!\n')
                return True

        except KeyError:
            error_num_garden_bed()

    def collect_ripe(self, num_potato_bed):
        print(f"Картошка с грядки {num_potato_bed} собрана, грядка пустая.")
        self.potatoes[num_potato_bed].clear()

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()


def error_num_garden_bed():

    print("Вы ввели неверный номер грядки, такого количества грядок нет.")
    option_2 = input(
        'Хотите посадить еще грядку? "да" - любой символ, "нет" - нажать "Enter": ')

    if option_2:
        num_potato_bed_new = len(garden.potatoes) + 1
        garden.potatoes[num_potato_bed_new] = [
            Potato(index) for index in range(1, count_potato + 1)
        ]


count_potato = int(input("Введите количество картошки на грядках: "))
count_potato_bed = int(input("Введите количество грядок: "))
garden = PotatoGarden(count_potato, count_potato_bed)


while True:

    num_potato_bed = int(
        input("Введите номер грядки за которой требуется уход: "))

    if garden.grow_all(num_potato_bed):
        num_potato_bed_for_control = int(
            input("Введите номер грядки, которую требуется проверить: "))

        if garden.are_all_ripe(num_potato_bed_for_control):
            option = input(
                'Собрать картофель? "да" - любой символ, "нет" - нажать "Enter": ')
            if option:
                garden.collect_ripe(num_potato_bed_for_control)
