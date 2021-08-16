import random
import string

letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation


letters_num = int(input('How many letters you want in your Password? '))
numbers_num = int(input('How many numbers you want in your Password? '))
special_num = int(input('How many special Characters you want in your Password? '))



password = ''

for i  in range(letters_num):
    password+= random.choice(letters)


for i  in range(numbers_num):
    password+= random.choice(numbers)


for i  in range(special_num):
    password+= random.choice(special_characters)
print(password)
mix_password = "".join(random.sample(password , len(password)))

print('your Password is :' ,mix_password)