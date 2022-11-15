# TODO здесь писать код

from random import shuffle


class Card:
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее
    suits = ("крести", "бубны", "пики", "червы")
    ranks = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "валет": 10,
        "дама": 10, "король": 10, "туз" : (1, 11)
    }



class Deck:
    #  Колода создаёт у себя объекты карт
    def __init__(self) -> None:
        self.deck = [
            (suit, *rank) for rank in Card.ranks.items() for suit in Card.suits
        ]

    def distribution_of_cards(self):
        if self.deck:
            shuffle(self.deck)
            return self.deck.pop()  # -> ("крести", "2", 2)
        else:
            return False



class Player:
    #  Игрок, у которого есть имя и какие-то карты на руках
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        self.score = 0

    def cards_on_hand(self, card):  # card -> ("крести", "2", 2)
        # добавляем карты на руки
        self.cards.append(" ".join(card[:2]))
        
        if card[1] == "туз":  # card -> ("крести", "туз", (1, 11))
            self.score += 11 if self.score + card[2][1] < 21 else 1
        else:
            self.score += card[2]

    def open_cards(self):
        text = "На руках у {} следующие карты: ".format(self.name) + ", ".join(self.cards) + "\nОчков {}".format(self.score)
        print(text)

    def clear_data(self):
        self.cards.clear()
        self.score = 0


class Computer(Player):
    def __init__(self, name="Компьютер") -> None:
        super().__init__(name)


def message_result(name, result):
    if result == "win":
        print(name, "выиграл!")
    else:
        print(name, "проиграл!")


deck = Deck()
computer = Computer()
name_player = input("Введите имя пользователя: ")
player = Player(name_player)
        
while True:

    player.clear_data()
    computer.clear_data()

    flag = True
    for _ in range(2):
        card_for_computer = deck.distribution_of_cards()
        card_for_player = deck.distribution_of_cards()

        if card_for_computer and card_for_player:
            computer.cards_on_hand(card_for_computer)
            player.cards_on_hand(card_for_player)
        else:
            flag = False
            break

    if flag:

        while True:

            print()
            player.open_cards()

            if player.score == 21:
                message_result(player.name, "win")
                break
            elif player.score > 21:
                message_result(player.name, "loss")
                break
            else:
                try:
                    option = int(input("Сдать карту? 1 - да, 0 - нет: "))
                    if option:
                        player.cards_on_hand(deck.distribution_of_cards())
                    elif player.score > computer.score:
                        print()
                        message_result(player.name, "win")
                        message_result(computer.name, "loss")
                        computer.open_cards()
                        # сделать вывод очков компьютера
                        break
                    elif player.score < computer.score:
                        print()
                        message_result(player.name, "loss")
                        message_result(computer.name, "win")
                        computer.open_cards()
                        # сделать вывод очков компьютера
                        break
                except ValueError:
                    print("Вы ввели неверный вариант!")
                    continue
    
        option_game = input("Хотите еще раздать карты? \"да\" - любой символ, \"нет\" - нажмите Enter: ")
        if option_game:
            continue
        else:
            break

    else:
        print("Колода пуста")
        break
