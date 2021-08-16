from random import choice , sample
from string import ascii_letters , digits , punctuation

letters = ascii_letters
numbers = digits
special_characters = punctuation


letters_num = int(input('How many letters you want in your Password? '))
numbers_num = int(input('How many numbers you want in your Password? '))
special_num = int(input('How many special Characters you want in your Password? '))



password = ''

for i  in range(letters_num):
    password+= choice(letters)


for i  in range(numbers_num):
    password+= choice(numbers)


for i  in range(special_num):
    password+= choice(special_characters)
print(password)
mix_password = "".join(sample(password , len(password)))

print('your Password is :' ,mix_password)