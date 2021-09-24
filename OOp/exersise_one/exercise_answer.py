from shirt import Shirt

'''TODO:\n",
    "#    - instantiate a shirt object with the following characteristics:\n",
    "#        - color red, size S, style long-sleeve, and price 25\n",
    "#    - store the object in a variable called shirt_one\n",'''

shirt_one = Shirt('red', 'S', 'long-sleeve', 25)

print('starting of Code...')

'''
 TODO:\n",
    "#     - print the price of the shirt using the price attribute\n",
    "#     - use the change_price method to change the price of the shirt to 10\n",
    "#     - print the price of the shirt using the price attribute\n",
    "#     - use the discount method to print the price of the shirt with a 12% discount\n",
'''
print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)

print(shirt_one.discount(0.12))

'''
ODO:\n",
    "#\n",
    "#    - instantiate another object with the following characteristics:\n",
    "# .       - color orange, size L, style short-sleeve, and price 10\n",
    "#    - store the object in a variable called shirt_two\n",
'''
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

'''
 TODO:\n",
    "#\n",
    "#    - calculate the total cost of shirt_one and shirt_two\n",
    "#    - store the results in a variable called total\n",
'''
print('Start oF Code ....')
total_cost = shirt_one.price + shirt_two.price
print(total_cost)

'''
### TODO:\n",
    "#\n",
    "#    - use the shirt discount method to calculate the total cost if\n",
    "#       shirt_one has a discount of 14% and shirt_two has a discount\n",
    "#       of 6%\n",
    "#    - store the results in a variable called total_discount\n",
'''
print('Start  of Code ....')
shirt_one_price = shirt_one.discount(0.14)
shirt_two_price = shirt_two.discount(0.06)

total_discount = shirt_one_price + shirt_two_price
print(total_discount)
