# TODO здесь писать код

zen_line = open("zen.txt", "r")
zen_list = zen_line.read().split("\n")
zen_list.reverse()
print(*zen_list, sep="\n")
zen_line.close()
