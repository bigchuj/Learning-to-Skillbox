# TODO здесь писать код

from statistics import mean


class Student:

    def __init__(self, 
                 initials=None,
                 group=None,
                 scores=None,
                 students=[]
                 ) -> None:
        
        self.initials = initials
        self.group = group
        self.scores = scores
        self.students = students
    
    
    def new_list_students(self):

        self.students.append(
            (mean(self.scores), self.initials, self.group)
        )


    def sort_students(self):
        
        self.students.sort()


    def out_result(self):
        
        print("Список студентов по возрастанию среднего балла:")
        [
            print(
                "Студент - {}, средний балл - {}, группа - {}".format(
                    student, score, group
                )
            ) for score, student, group in self.students
        ]


students_ = [
    ("Ivan Ivanov", 3, [3, 2, 4, 4, 3]),
    ("Valentina Petrova", 5, [4, 5, 5, 3, 5]),
    ("Petr Petrov", 2, [3, 3, 3, 4, 4]),
    ("Kostya Vasin", 2, [3, 3, 3, 4, 4]),
    ("Svetlana Fomina", 4, [5, 5, 3, 5, 4]),
    ("Vlad Smirnov", 3, [1, 4, 5, 5, 1]),
    ("Evgeniy Soboplev", 1, [2, 4, 1, 3, 5]),
    ("Nina Dmitrieva", 5, [5, 5, 5, 5, 5]),
    ("Evgeniy Gavrilin", 1, [4, 1, 4, 3, 2]),
    ("Anastasiya Filimonova", 4, [5, 4, 3, 1, 5])
]

for student in students_:

    means_st = Student(*student)
    means_st.new_list_students()

sort_st = Student().sort_students()
result_print = Student().out_result()
