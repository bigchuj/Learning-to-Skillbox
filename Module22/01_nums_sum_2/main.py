# TODO здесь писать код

text = open("numbers.txt", "r")
line = text.read()
print("Содержимое файла numbers.txt", line, sep="\n")
line_list = [int(i.strip()) for i in line.split("\n") if i != ""]
summ = sum(line_list)
text.close()

new_file = open("answer.txt", "w")
new_file.write(str(summ))
new_file.close()

num = open("answer.txt", "r")
print("\nСодержимое файла answer.txt", num.read(), sep="\n")
num.close()
