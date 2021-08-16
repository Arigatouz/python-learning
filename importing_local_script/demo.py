import random
import another_module as nm

list_of_numbers = [15, 16, 7, 18, 19, 20, 25, 24, 36, 33]
add_three = nm.add_three(list_of_numbers, 1)
print(add_three)

find_average = nm.average(list_of_numbers)
print(int(find_average))


print(__name__)
print(nm.__name__)


# Quiz: Password Generator
'''
Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. Your function should not accept any arguments and should reference the global variable word_list to build the password.
'''
# TODO: First import the `random` module

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open('importing_local_script/password.txt', 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)
print(word_list)
# TODO: Add your function generate_password below
# It should return a string consisting of three random words
# concatenated together without spaces

# we import the random library up then we start working on the function


def generate_password():
    #  '''First attempt'''
    #     # random_words = random.choices(word_list , k =3)
    #     # for word in random_words:
    #     #     print(word)
    # '''second attempt'''
    #     # return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
    # '''third attempt'''
    return ''.join(random.sample(word_list, 3))


# Now we test the function
generate_password()
print(generate_password())


'''
Which Module? 1
Which module can tell you the current time and date?

datetime

Which Module? 2
Which module has a method for changing the current working directory?

os.path

Which Module? 3
Which module can read data from a comma separated values (.csv) file into Python dictionaries for each row?

csv


Which Module? 4
Which module can help extract all of the files from a zip file?

zipfile


Which Module? 5
Which module can say how long your code took to run?

time it


Our favorite modules
The Python Standard Library has a lot of modules! To help you get familiar with what's available, here are a selection of our favourite Python Standard Library modules and why we use them!

csv: very convenient for reading and writing csv files
"https://docs.python.org/3/library/csv.html"

collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
"https://docs.python.org/3/library/collections.html"

random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
"https://docs.python.org/3/library/random.html"

string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
"https://docs.python.org/3/library/string.html"

re: pattern-matching in strings via regular expressions
"https://docs.python.org/3/library/re.html"

math: some standard mathematical functions
"https://docs.python.org/3/library/math.html"

os: interacting with operating systems
"https://docs.python.org/3/library/os.html"

os.path: submodule of os for manipulating path names
"https://docs.python.org/3/library/os.path.html"

sys: work directly with the Python interpreter
"https://docs.python.org/3/library/sys.html"

json: good for reading and writing json files (good for web work)
"https://docs.python.org/3/library/json.html"
'''
