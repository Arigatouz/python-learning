print(float(15 / 7))

my_name = "Ali "
my_father_name = "Gamal"
print(my_name + my_father_name)
my_length_name = ((my_name + my_father_name + " --- ") * 5)

print(my_length_name)
print(len(my_length_name))

print(float(len(my_length_name) / 15))

just_string = '''hello from the "other side" right my 'nigga' '''
print(just_string)

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + " " + middle_names + " " + family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

# random list aka array

random_items = [1, 2, True, 'Dragon', "Rider", 5.2, {'katarina': 'Fail'}]

print(random_items[3])
print(random_items[0])
print(random_items[:6])
print(type(random_items[2]))
print(random_items[:3])
part_array = random_items[2:6]
print(part_array)
another_value = random_items[6].values()
print(type(another_value))

print("sunday" in random_items)
print("sunday" not in random_items)

# this should return true or false
print('1' not in random_items)
print(1 in random_items)

month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month - 1]

print(num_days)

name = "Ali"
print(name[0])

# TRY len() and max() sorted( the sorted , reverse = True) on list

numbers_array = [98, 15, 24, 68, 74, 95, 345, 45, 74]

# really good one to get the last element of the list aka array
print(numbers_array[len(numbers_array) - 1])

print(len(numbers_array))
print(sorted(numbers_array))
print(sorted(numbers_array, reverse=True))
numbers_array.sort()
print(numbers_array)

print(max(numbers_array))
print(min(numbers_array))

punch_of_letters = (["fore", "after", "starboard", "port"])
new_line_letters = "\n".join(punch_of_letters)
print(new_line_letters)

hyphen_letters = "-".join(punch_of_letters)
print(hyphen_letters)

new_punch_letters = punch_of_letters
new_punch_letters.append('DRAGONRIDER')
print(new_punch_letters)

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

# now we will try tuples

coordination = (15.3541, 16.2356747)
print('the longitude of the area is: {} and the latitude is: {}'.format(
    coordination[0], coordination[1]))

dimensions = (42, 35, 71)
width, height, length = dimensions
message = "the width is {} , height is {} and length is {}".format(
    width, height, length)
print(message)

# using sets

fruit = ["apple", "banana", "orange", "grapefruit", "banana", "apple"]
unique_fruit = set(fruit)
print(fruit)
print(unique_fruit)  # it makes the items unique

unique_fruit.add('watermelon')  # add element to the set randomly
print(unique_fruit)
# remove element from the set randomly
unique_fruit.pop()
print(unique_fruit)
# union method on sets it takes an array/arrays as an arguments and then it add them to a new set but the ordinal set
# is the same
uncrowned_fruit = unique_fruit.union(['mango', "beef"], ['katarina', 'Django'])
print(uncrowned_fruit)
# intersection it needs iterable or mutable to be compared
intersected_fruit = unique_fruit.intersection(['watermelon', "banana"])
print(unique_fruit)
print(intersected_fruit)

# difference  it compares the left statement to the right if the elements on the left are in the right side #and it
# returns the vales that not exist on the right side
# it has many ways to compare look examples down  can use  {} or  [] or () or key value pairs
# but when using key value pairs don't forget to add the value method at the end

# diff_fruit = unique_fruit.difference(['banana', 'watermelon'])
# diff_fruit = unique_fruit.difference({'banana', 'watermelon'})
# diff_fruit = unique_fruit.difference(('banana', 'watermelon'))
diff_fruit = unique_fruit.difference(
    {"key_a": "banana", "key_b": "watermelon"}.values())
print(diff_fruit)
print(unique_fruit)
# dictionaries are mutable data type that stores mappings of unique keys to values. Here's a dictionary that
# stores elements and their atomic numbers.


print('____________________________________________________________________')
print('end')
print('---------------------------------------------------------------------')
# name[2] = "ss"
# print(name)  # it will give u an error because you cant change the value of a strting
