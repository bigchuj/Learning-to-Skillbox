# TODO здесь писать код

from copy import deepcopy


class Parent:
    
    def __init__(self, name=None, age=None, kids={}) -> None:
        
        self.name = name
        self.age = age
        self.kids = kids
        self.reactions_to_state_of_calm_kids = {
            "Спокоен": "Вместе радуемся хорошему настроению",
            "Нервничает": "Глажу ребенка по голове, целую в щеку",
            "Плачет": "Беру на руки и успокаиваю"
        }
        self.reactions_to_state_of_hunger_kids = {
            "Голодный": "Покормить ребенка",
            "Сытый": "Отправить ребенка играть"
        }


    def info_about_yourself(self):
        # печатает параметры о себе и списком выводит детей с их параметрами

        line = f"\nИмя родителя {self.name}, его возраст {self.age}. Дети:\n"

        def out_info(elem, num=1):

            line_ = []
            if isinstance(elem, dict):

                for key in elem.keys():
                    line_.append("  " * num + str(key) + "\n")
                    line_.append(out_info(elem.get(key), num + 1))

            else:
                line_.append("  " * num + str(elem) + "\n")

            return " ".join(line_)
        
        line += out_info(self.kids)
        print(line)


    def reaction_to_state_of_calm_kid(self, state_of_calm_kid, number_kid):
        # реакция на состояние спокойствия ребенка

        reaction = self.reactions_to_state_of_calm_kids[state_of_calm_kid]
        print("Реакция родителя на состяние ребенка:", reaction)
        self.kids[number_kid]["Состояние спокойствия:"] = {
                "начальное состояние:": state_of_calm_kid,
                "реакция родителя:": reaction
        }

        if state_of_calm_kid != "Спокоен":
            self.kids[number_kid]["Состояние спокойствия:"]["новое состояние:"] = "Ребенок спокоен"
        
    
    def reaction_to_state_of_hunger_kid(self, state_of_huger_kid, number_kid):
        # реакция на состояние голода ребенка 

        reaction = self.reactions_to_state_of_hunger_kids[state_of_huger_kid]
        print("Реакция родителя на состяние ребенка:", reaction)
        self.kids[number_kid]["Состояние голода:"] = {
            "начальное состояние:": state_of_huger_kid,
            "реакция родителя:": reaction
        }

        if state_of_huger_kid != "Сытый":
            self.kids[number_kid]["Состояние голода:"]["новое состояние:"] = "Ребенок сытый"


    def add_kids(self, name_kid, age_kid, number_kid):
        # добавление ребенка в список детей

        self.kids[number_kid] = {
            "Имя:": name_kid, "возраст:": age_kid
        }


class Kid:
    
    def __init__(self, name, age, number_kid, parent=None) -> None:
        
        self.name = name
        self.age = age
        self.number_kid = number_kid
        self.parent = parent
        self.number_kids = {
            1: "\n  Первый ребенок:", 2: "\n  Второй ребенок:", 3: "\n  Третий ребенок:",
            4: "\n  Четвертый ребенок:", 5: "\n  Пятый ребенок:", 6: "\n  Шестой ребенок:",
            7: "\n  Седьмой ребенок:", 8: "\n  Восьмой ребенок:", 9: "\n  Девятый ребенок:",
            10: "\n  Десятый ребенок:"
        }
        self.states_of_calm = {
            1: "Спокоен",
            2: "Нервничает",
            3: "Плачет"
        }
        self.states_of_hunger = {
            1: "Голодный",
            2: "Сытый"
        }
        self.parent.add_kids(self.name, self.age, self.number_kids[self.number_kid])


    def state_of_calm_(self) -> str:
        # состояние спокойствия
        while True:
            try:
                print("\nКакой уровень спокойствия ребенка?")
                state = int(
                    input("1 - спокоен, 2 - нервничает, 3 - плачет:\n")
                )

                self.parent.reaction_to_state_of_calm_kid(
                    self.states_of_calm[state], self.number_kids[self.number_kid]
                )
                break
            except:
                print("Ошибка ввода, попробуйте снова")


    def state_of_hunger_(self):
        # состoяние голода
        while True:
            try:
                state = int(
                    input("\nРебенок голодный? 1 - да, 2 - нет: ")
                )
                self.parent.reaction_to_state_of_hunger_kid(
                    self.states_of_hunger[state], self.number_kids[self.number_kid]
                )
                break
            except:
                print("Ошибка ввода, попробуйте снова")

        
class Administration:

    def __init__(
        self, parents_and_kids={}, 
        count_parent=0, count_kid=0
    ) -> None:
        
        self.parents_and_kids = parents_and_kids
        self.count_parent = count_parent
        self.count_kid = count_kid
    

    def parents(self):

        while True:

            self.count_kid = 0
            self.count_parent += 1
            name_parent = input("\nВведите имя родителя или 'Enter' для окончания ввода: ")

            if name_parent:
                
                age_parent = int(input("Введите возраст: "))
                parent = deepcopy(Parent(name_parent, age_parent))
                
                while True:
                    
                    name_kid = input("\nВведите имя ребенка или 'Enter' для окончания ввода: ")
                    
                    if name_kid:

                        while True:  # проверка на возраст
                            
                            self.count_kid += 1
                            age_kid = int(input("Введите возраст: "))

                            if age_parent - age_kid < 16:

                                print(
                                    "Возраст ребенка должен быть меньше возраста родителя хотя бы на 16 лет."
                                )
                                continue

                            break

                        kid = Kid(name_kid, age_kid, self.count_kid, parent)
                        kid.state_of_calm_()  # состояние спокойствия
                        kid.state_of_hunger_()  # состояние голода
                    
                    else:
                        break        
            
                # написать вывод информации о родителе
                self.parents_and_kids[self.count_parent] = parent
                option = input("Вывести информацию о родителе (да/нет)? ").lower()
                if option == "да":
                    parent.info_about_yourself()

            else:
                break

    def print_family_tree(self):

        for num, cl in self.parents_and_kids.items():

            print(f"\nИнформация о генеалогической ветки номер {num}:")
            cl.info_about_yourself()


start = Administration()
start.parents()
start.print_family_tree()


# parents_and_kids = {}
# count_parent = 0  # счетчик веток родителей

# while True:

#     count_kid = 0  # счетчик количетсва детей
#     count_parent += 1
#     name_parent = input("\nВведите имя родителя или 'Enter' для окончания ввода: ")

#     if name_parent:
        
#         age_parent = int(input("Введите возраст: "))
#         parent = deepcopy(Parent(name_parent, age_parent))
        
#         while True:
            
#             name_kid = input("\nВведите имя ребенка или 'Enter' для окончания ввода: ")
            
#             if name_kid:

#                 while True:  # проверка на возраст
                    
#                     count_kid += 1
#                     age_kid = int(input("Введите возраст: "))

#                     if age_parent - age_kid < 16:

#                         print(
#                             "Возраст ребенка должен быть меньше возраста родителя хотя бы на 16 лет."
#                         )
#                         continue

#                     break

#                 kid = Kid(name_kid, age_kid, count_kid, parent)
#                 kid.state_of_calm_()  # состояние спокойствия
#                 kid.state_of_hunger_()  # состояние голода
            
#             else:
#                 break        
    
#         # написать вывод информации о родителе
#         parents_and_kids[count_parent] = parent #deepcopy(parent)
#         option = input("Вывести информацию о родителе (да/нет)? ").lower()
#         if option == "да":
#             parent.info_about_yourself()
#     else:
#         break



# print()

# for num, cl in parents_and_kids.items():

#     print(f"\nИнформация о генеалогической ветки номер {num}:")
#     cl.info_about_yourself()

