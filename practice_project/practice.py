# quiz
'''
Practice Question
For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main(separate) function should take user input(user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter(from dictionary created in the first function).

Sample Output:

>>> Enter your First[space] Last name only: Bill Newman
>>> Unique flower name with the first letter: Bellflower

'''

# Write your code here
# HINT: create a dictionary from flowers.txt


def get_flowers_name(flower_name):
    flower_dict = {}
    with open(flower_name, 'r') as flower_list:
        for flower in flower_list:
            # print(flower)
            flower_key = flower.split(": ")[0].lower()
            flower_value = flower.split(": ")[1].strip()
            # print(flower_key, flower_value)
            flower_dict[flower_key] = flower_value
        return flower_dict


# HINT: create a function to ask for user's first and last name


# def get_full_name():
#     first_name = input('Enter Your First Name : ').strip()
#     Last_name = input('Enter Your Last Name : ').strip()
#     flower_extracted_dict = get_flowers_name('flowers.txt')
#     for flower_key, flower_value in flower_extracted_dict.items():
#         if first_name[0].lower() == flower_key.lower():
#             result = "Unique flower name with the first letter: {}".format(
#                 flower_value)
#             print(result)
#             break
#         else:
#             result = "Wrong input please make sure you "

# get_full_name()
# print the desired output

'''
# another way
'''


def get_full_name():
    while Exception:
        try:
            flower_d = get_flowers_name('flowers.txt')
            full_name = input(
                "Enter your First [space] Last name only: ").strip()
            first_name = full_name[0].lower()
            first_letter = first_name[0]
    # print command that prints final input with value from corresponding key in dictionary
            print("Unique flower name with the first letter: {}".format(
                flower_d[first_letter]))
            break
        except Exception as e:
            print('you entered Wrong value : {}'.format(e))


get_full_name()
