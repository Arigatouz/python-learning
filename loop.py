cities = ["cairo", "giza", "tanta", "elbe7ara"]
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

# i = 1
# while i < 3:
#     print(i)

# we can create list through Range
# range(start ,  stop , step) used to create immutable sequences of numbers

for i in range(3):
    print(i)
print("---" * 3)
for j in range(2, 6):
    print(j)
print("---" * 3)
for k in range(1, 10, 2):
    print(k)
print("---" * 3)
for _ in range(3):
    print('Hello')
print("---" * 3)

for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)

# quiz
sentence = ["the", "quick", "brown", "fox",
            "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print(word)

# quiz
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5, 35, 5):
    print(i)

# quiz
"""Quiz: Create Usernames Write a for loop that iterates over the names list to create a usernames list. To create a
username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the
list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should create the list:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

HINT: Use the .replace() method to replace the spaces with underscores. Check out how to use this method in this
Stack Overflow answer. https://stackoverflow.com/questions/12723751/replacing-instances-of-a-character-in-a-string
/12723785#12723785 """

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.replace(" ", "_")
    usernames.append(name.lower())
print(usernames)

# important
"""The printed output for the another_names list will look exactly like it did in the first line. During each
iteration, the name variable is set to a string taken from the list. Then the assignment statement creates a new
string (name.lower().replace(" ", "_")) and changes the name variable to that string. It doesn't modify the contents
of the another_names list at all. To modify the list you must operate on the list itself, using range, as you saw
earlier. """
another_names = ["Joey Tribbiani", "Monica Geller",
                 "Chandler Bing", "Phoebe Buffay"]

for name in another_names:
    name = name.lower().replace(" ", "_")

print(another_names)

# to fix this we need to do this
for index in range(len(another_names)):
    another_names[index] = another_names[index].replace(" ", "_").lower()
print(another_names)

# quiz
"""Quiz: Tag Counter Write a for loop that iterates over a list of strings, tokens, and counts how many of them are
XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left
angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings.
"""

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

for token in tokens:
    if token.__contains__('<') and token.__contains__('>'):
        count += 1
        print(token)

print(count)

# quiz
"""Quiz: Create an HTML List Write some code, including a for loop, that iterates over a list of strings and creates
a single string, html_str, which is an HTML list. For example, if the list is items = ['first string',
'second string'], printing html_str should output:

<ul> <li>first string</li> <li>second string</li> </ul> That is, the string's first line should be the opening tag
<ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of
the string should be the closing tag </ul>. """

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

print(list(range(0, -5)))

# looping around list and adding to dictionary
book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
              'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

# another quiz
""" You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.
"""
output = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for key, value in basket_items.items():
    if key in fruits:
        output += value
# if the key is in the list of fruits, add the value (number of fruits) to output


print(output)

# Quiz: Fruit Basket - Task 3
"""
So, a couple of things about the above examples:

It is a bit annoying having to copy and paste all the code to each spot - wouldn't it be nice to have a way to repeat
the process without copying all the code? Don't worry! You will learn how to do this in the next lesson!


It would be nice to keep track of both the number of fruits and other items in the basket.

Use the environment below to try out this second part.
"""
# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for key, value in basket_items.items():
    # if the key is in the list of fruits, add to fruit_count.
    if key in fruits:
        fruit_count += value
    # if the key is not in the list, then add to the not_fruit_count
    elif key not in fruits:
        not_fruit_count += value

print(fruit_count, not_fruit_count)

hand_card = [4, 32, 24, 8, 7, 6, 9, 1, 4, 2, 3, 4]
hand = []

while sum(hand) <= 30:
    hand.append(hand_card.pop())

print(hand)

# factorial number
# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(1, number + 1):
    # we all 1 in range coz every thing we multiply with  zero = zero and the (number  + 1 )  the number = 6 so the
    # list will stop at 5 so we need the number to equal it's original equality so we add 1
    product *= num

# print the factorial of number
print(product)

# quiz

'''Suppose you want to count from some number start_num by another number count_by until you hit a final number
end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that
end_num is always larger than start_num and count_by is always positive.

Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through
the loop? What condition will you use to see when it's time to stop looping?

After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the
case that break_num should be a number that is the first number larger than end_num. '''

start_num = 2  # provide some start number
end_num = 10  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by

# write a while loop that uses break_num as the ongoing number to
break_num = start_num
while break_num <= end_num:
    break_num += count_by

#   check against end_num


print(break_num)


# Quiz: Nearest Square
'''Write a while loop that finds the largest square number less than an integrate and stores it in a variable
nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number
because it equals 6*6.

For example, if limit is 40, your code should set the nearest_square to 36.'''
limit = 40

# write your while loop here
num = 0

while (num + 1) ** 2 < limit:
    num += 1
nearest_square = num ** 2
print(nearest_square)


# Example on break and continue in loops
manifest = [("bananas", 15), ("mattresses", 24),
            ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

'''
Quiz: Break the String
Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.
'''
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
word_lens = 0
# write your loop here
for word in headlines:
    print('the word length now is {}'.format(word_lens))
    if word_lens <= 140:
        print(len(word))
        word_lens += len(word)
        news_ticker += word
        print(word_lens)
    else:
        break
news_ticker = news_ticker[:140]
print(news_ticker)
print(len(news_ticker))


'''
Coding Quiz: Check for Prime Numbers
Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

For instance, 6 has four factors: 1, 2, 3, 6.
1 X 6 = 6
2 X 3 = 6
So we know 6 is not a prime number.

In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

If the numbers are prime, the code should print "[number] is a prime number."
If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".
Example output:

7 IS a prime number
26 is NOT a prime number, because 2 is a factor of 26
'''

# Your code should check if each number in the list is a prime number
# write your code here
# HINT: You can use the modulo operator to find a factor
check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

    # search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

        # number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(
                num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num - 1:
            print("{} IS a prime number".format(num))
