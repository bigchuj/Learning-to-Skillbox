alphabet = 'abcdefg'

# TODO здесь писать код

line_copy = alphabet[:]  # 1
print("1:", line_copy)

line_reverse = alphabet[::-1]  # 2
print("2:", line_reverse)

line_every_second_elem_1 = alphabet[::2]  # 3
print("3:", line_every_second_elem_1)

line_every_second_elem_2 = alphabet[1::2]  # 4
print("4:", line_every_second_elem_2)

elem_before_second = alphabet[:1]  # 5
print("5:", elem_before_second)

elem_before_penultimate = alphabet[-1:-2:-1]  # 6
print("6:", elem_before_penultimate)

elem_in_range_3_4_exclusive = alphabet[3:4]  # 7
print("7:", elem_in_range_3_4_exclusive)

elem_last_three = alphabet[-3:]  # 8
print("8:", elem_last_three)

elem_in_range_3_4_inclusive = alphabet[3:5]  # 9
print("9:", elem_in_range_3_4_inclusive)

elem_in_range_3_4_inclusive_reverse = alphabet[4:2:-1]  # 10
print("9:", elem_in_range_3_4_inclusive_reverse)
