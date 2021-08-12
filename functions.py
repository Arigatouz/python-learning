#Quiz: readable_timedelta
'''
Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

print(readable_timedelta(10))
should output the following:

1 week(s) and 3 day(s).
'''
# write your function here

def readable_timedelta(days):
    weeks = days /7
    weeks_int = int(weeks)
    remaning_days = days % 7
    message = "{} week(s) and {} day(s).".format(weeks_int , remaning_days)
    return message
# test your function
print(readable_timedelta(15))

print('===' * 30)
# scope variables in function 
x = 4
def add_numbers(num):
    '''we cant call the num and print it here coz the variable scope so we need 
    to call x after the function ends and equal to the out put of the function as 
    shown down there '''
    num += 12
    return num
x  = add_numbers(x)
print(x)

print('===' * 30)

# Quiz: Write a Docstring
'''
Write a docstring for the readable_timedelta function you defined earlier! Remember the way you write your docstrings is pretty flexible! Look through Python's docstring conventions here and check out this Stack Overflow page for some inspiration!
'''


def readable_timedelta(days):
    # insert your docstring here
    '''
    calculating weeks and days in a number function
    input:
    is the number of days you want to calculate how many weeks and days left out of that number
    prossing with 
    weeks:
    divided by 7 and getting the divided  number with an int not a float
    reminder :
    which is the module of 7  to calculate how many days left after calculating weeks
    ourput:
    the number of wees and the number of days  in a string message 
    '''
    weeks = days // 7

    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


print('===' * 30)

# Quiz: Lambda with Map
'''
map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().
'''
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]


def mean(num_list): return sum(num_list) / len(num_list)


averages = list(map(mean, numbers))
print(averages)


print('===' * 30)


# Quiz: Lambda with Filter
'''
filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().
'''
cities = ["New York City", "Los Angeles",
          "Chicago", "Mountain View", "Denver", "Boston"]


def is_short(city): return len(city) < 10


short_cities = list(filter(is_short, cities))
print(short_cities)

print('===' * 30)
