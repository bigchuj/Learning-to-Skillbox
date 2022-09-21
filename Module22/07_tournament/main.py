# TODO здесь писать код


def selection_of_participants(num_sel, participants_list):

    # формируем список с участниками следующего этапа, данные в кортеже:
    # "счет", "инициал имени фамилия" 

    participants_next_tour = []
    participants_list_corrected = [par.split() for par in participants_list]

    for surname, name, score in participants_list_corrected:

        if int(score) > num_sel:
            participants_next_tour.append((score, name[0] + '. ' + surname))

    return participants_next_tour


def sort_participants(participants_list):

    result = []
    participants_list.sort(reverse=True)

    for i_place, elem in enumerate(participants_list):
        result.append(str(i_place + 1) + ") " + elem[1] + " " + elem[0])

    return result


# read file with participants
line_1 = open("first_tour.txt", "r")
texts = line_1.read().split("\n")
print("Содержимое файла first_tour.txt:", *texts, sep="\n")
participants_next_tour = sort_participants(
    selection_of_participants(int(texts[0]), texts[1:])
) 
line_1.close()

# write file with participants
line_2 = open("second_tour.txt", "a")
line_2.write(str(len(participants_next_tour)) + "\n")

for elem in participants_next_tour:
    line_2.write(elem + "\n")

line_2.close()

# read finished file
line_3 = open("second_tour.txt", "r")
print("\nСодержимое файла second_tour.txt:", line_3.read(), sep="\n")
line_3.close()
