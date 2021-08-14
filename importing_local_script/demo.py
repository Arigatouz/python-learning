import another_moduel as nm

list_of_numbers = [15, 16, 7, 18, 19, 20, 25, 24, 36, 33]
add_three = nm.add_three(list_of_numbers, 1)
print(add_three)

find_average = nm.average(list_of_numbers)
print(int(find_average))


print(__name__)
print(nm.__name__)
