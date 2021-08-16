from random import choice as randomchoice , sample as randomsample
from string import ascii_letters , digits , punctuation



letters = ascii_letters
numbers = digits
special_characters = punctuation


letters_num = int(input('How many letters you want in your Password? '))
numbers_num = int(input('How many numbers you want in your Password? '))
special_num = int(input('How many special Characters you want in your Password? '))



password = ''

for i  in range(letters_num):
    password+= randomchoice(letters)


for i  in range(numbers_num):
    password+= randomchoice(numbers)


for i  in range(special_num):
    password+= randomchoice(special_characters)
print(password)
mix_password = "".join(randomsample(password , len(password)))

print('your Password is :' ,mix_password)

