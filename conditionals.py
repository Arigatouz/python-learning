# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin


"""
All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Oh dear, no prize this time."

Note: Feel free to test run your code with other inputs, but when you submit your answer, only use the original input of points = 174. You can hide your other inputs by commenting them out.
"""
points = 130  # use this input to make your submission
result = ""
# write your if statement here
if points < 1:
    result = "ZERO OR MINUS"
elif 1 <= points <= 50:
    result = "wooden rabbit"
elif 51 <= points <= 150:
    result = "no prize"
elif 151 <= points <= 180:
    result = "wafer-thin mint"
else:
    result = "penguin"
# checking the result out put
if result == "no prize":
    message = "Oh dear, no prize this time."
else:
    message = "Congratulations! You won a " + result + "!"


print(message)


# quiz
'''
You decide you want to play a game where you are hiding a number from someone. Store this number in a variable called 'answer'. Another user provides a number called 'guess'. By comparing guess to answer, you inform the user if their guess is too high or too low.

Fill in the conditionals below to inform the user about how their guess compares to the answer.
'''
# '''

# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 15  # provide answer
guess = 10  # provide guess

if answer > guess:  # provide conditional
    result = "Oops!  Your guess was too low."
elif answer < guess:  # provide conditional
    result = "Oops!  Your guess was too high."
elif answer == guess:  # provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)


# another quiz
'''
Depending on where an individual is from we need to tax them appropriately. The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. Use this information to take the amount of a purchase and the corresponding state to assure that they are taxed by the right amount.
'''
# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "CA"  # Either CA, MN, or NY
purchase_amount = 1500  # amount of purchase

if state == "CA":  # provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

elif state == "MN":  # provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

elif state == "NY":  # provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state, total_cost)

print(result)


"""
Here are most of the built-in objects that are considered False in Python:

constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '"", (), [], {}, set(), range(0)
"""
# another quiz
"""
You will use a new variable prize to store a prize name if one was won, and then use the truth value of this variable to compose the result message. This will involve two if statements.

1st conditional statement: update prize to the correct prize name based on points.
2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.

If prize is None, result should be set to "Oh dear, no prize this time."
If prize contains a prize name, result should be set to "Congratulations! You won a {}!".format(prize). This will avoid having the multiple result assignments for different prizes.
At the beginning of your code, set prize to None, as the default value.
"""

points = 134  # use this as input for your submission

# establish the default prize value to None

prize = None
# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    prize = "Oh dear, no prize this time."
elif points <= 180:
    prize = "wafer-thin mint"
else:
    prize = "penguin"
# use the truth value of prize to assign result to the correct prize
if prize == "Oh dear, no prize this time.":
    result = "Oh dear, no prize this time."
else:
    result = "Congratulations! You won a {}!".format(prize)
print(result)
