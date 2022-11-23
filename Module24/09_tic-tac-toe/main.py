# TODO здесь писать код

from random import shuffle  # choices


class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self, number) -> None:
        self.number = str(number)
        self.status = True  # -> свободна

    def status_cell(self):
        return self.status

    def value_cell(self, number):
        # меняем значение в ячейке и ее статус
        if number in "xх":
            number = "x"
        elif number in "oо0":
            number = "o"
        self.number = number
        self.status = False


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    cell_coordinates = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2)
    }

    def __init__(self) -> None:
        self.board = self.__filling_board()

    def __filling_board(self):
        # наполняем поле клетками - матрица
        board = []
        counter = 0
        for _ in range(3):
            temp_list = []
            for _ in range(3):
                counter += 1
                temp_list.append(Cell(counter))
            board.append(temp_list)
        return board
    
    def __check_len(self, value) -> bool:
        return len(value) == 1

    def corrected_cell(self, number_cell, value_cell):
        # корректируем статус ячейки и ее значение
        num_line, num_colum = self.cell_coordinates[number_cell]
        cell = self.board[num_line][num_colum]
        if cell.status_cell():  # -> если ячейка свободная, то передаем ей новое значение
            cell.value_cell(value_cell)
            return True  # запись значения удачна
        else:
            return False  # ячейка занята

    def check_board(self):
        
        value_main_diagonals = set()
        for elem_i in range(len(self.board)):

            value_main_diagonals.add(self.board[elem_i][elem_i].number)  # добавляем значения главной диагонали для дальнейшей проверки
            
            value_line = set(elem.number for elem in self.board[elem_i])
            if self.__check_len(value_line): return True  # если в строке все значения одинаковы       

            value_collum = set()  # значения столбцов
            value_sec_diagonals = set()  # значения побочной диагонали

            for elem_j in range(len(self.board[elem_i])):
                value_collum.add(self.board[elem_j][elem_i].number)

                if not elem_i:
                    value_sec_diagonals.add(self.board[elem_j][-elem_j - 1].number)

            if self.__check_len(value_collum) or self.__check_len(value_sec_diagonals): return True
        
        if self.__check_len(value_main_diagonals): return True


    def out_board(self): 
        # вывод игрового поля на экран 
        # -> [
        #     [Cell('1'), Cell('2'), Cell('3')],
        #     [Cell('4'), Cell('5'), Cell('6')],
        #     [Cell('7'), Cell('8'), Cell('9')]
        # ]
        # Cell().number() -> 1, 2, 3 ... 
        print(" ___________")
        for cells in self.board:
            values = [cell.number for cell in cells]
            print("|_" + "_|_".join(values) + "_|")


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self, name) -> None:
        self.name = name

    def go_to_cell(self, board):

        while True:
            try:
                cell_num, cell_value = input(
                    'Введите номер ячейки и значение ("x" или "0") через пробел: ').lower().split()
                if cell_num in "123456789" and cell_value in "xoхо0":  # en, ru, 0
                    if board.corrected_cell(cell_num, cell_value):
                        board.out_board()
                        break
                    else:
                        print("Данная ячейка занята, попробуйте другую.\n")
                        board.out_board()
                        continue
                else:
                    raise ValueError

            except ValueError:
                print("Вы ввели неверные значения, проверьте пожалуйста ввод и повторите снова")
                continue

    def winner(self):
        print(self.name, "выиграл!")


def check_counter(counter):
    if counter == 9:
        print("Игра окончена.")
        return True


while True:
    board = Board()
    input("\n~~~ Нажмите Enter для начала игры. ~~~\n")
    player_1 = Player(
        name=input("Введите имя первого игрока: ")
    )
    player_2 = Player(
        name=input("Введите имя второго игрока: ")
    )
    print("Система случайным образом определит, кто будет ходить первый.")
    players = [player_1, player_2]
    shuffle(players)
    first_move, second_move = players

    counter = 0
    while True:
        # вывод игрового поля:
        board.out_board()
        
        counter += 1
        print("Ходит игрок:", first_move.name)
        first_move.go_to_cell(board)
        if board.check_board(): 
            first_move.winner()
            break
        if check_counter(counter): break
        
        counter += 1
        print("Ходит игрок:", second_move.name)
        second_move.go_to_cell(board)
        if board.check_board(): 
            second_move.winner()
            break
        if check_counter(counter): break
