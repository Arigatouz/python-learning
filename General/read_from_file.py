
import math as MT
with open("camelot.txt" ,'r') as song:
    file_data = song.read()
    print(song.read(2))
    print(song.read(8))
    print(song.read())
# you cant access  song from out the indentation
# but you can access file_data from anywhere
print(file_data.find('we'))
print(file_data)

list_of_lines = list()
with open("./text_file.txt" , 'r') as f:
    for line in f:
        list_of_lines.append(line.strip())


print(list_of_lines)


for line in list_of_lines:
    print(line, list_of_lines.index(line))


# quiz Quiz: Flying Circus Cast List
'''
You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com). Each line of that file consists of an actor's name, a comma, and then some(messy) information about roles they played in the programme. You'll need to extract only the name and add it to a list. You might use the .split() method to process each line.
'''


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename , 'r') as actors_list:

        # use the for loop syntax to process each line
        for actor in actors_list:
            cast_list.append(actor.split(',')[0])
    # and add the actor name to cast_list

    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor, cast_list.index(actor) + 1)


# MT refears to the imported module from math 
#at the begining of the page
factorial_four = MT.factorial(4)
print(factorial_four)

