while True:
    try:
        loan_amount = int(input('Enter the Loan amount you need : '))
        taxes = 13
        the_final_amount_of_money_to_pay = (loan_amount * taxes) / 100
        print(the_final_amount_of_money_to_pay)
        break
    except ValueError as erroz:
        print('\n the input is invalid {} '.format(erroz))
    except KeyboardInterrupt as btn:
        # i cant get the hash of the error but i dont know how can i use this to be in a usefull case tho :D maybe you will find :D
        # love you :D
        print('User Asks to quit the program {}'.format(btn.__hash__()))
        break
    finally:
        print('thanks for using our App')

print('NEXT QUIZ')
# Quiz Handling Input Errors
'''
The party_planner function below takes as input a number of party people and cookies and figures out how many cookies each person gets at the party, assuming equitable distribution of cookies. Then, it returns that number along with how many cookies will be left over.

Right now, calling the function with an input of 0 people will cause an error, because it creates a ZeroDivisionError exception. Edit the party_planner function to handle this invalid input. If it runs into this exception, it should print a warning message to the user and request they input a different number of people.

After you've edited the function, try running the file again and make sure it does what you intended. Try it with several different input values, including 0 and other values for the number of people.

Using this workspace
In some pages of our classroom, we'll provide you a workspace like the one below that will provide you a programming environment with a Terminal and code editor, so you can do all your work right here. Here are a few tips orienting you to this kind of workspace.

On the top panel is a code editor where you can edit your Python file. Scroll up and down in this panel to see all the code. You can also expand or shrink this panel by clicking and dragging its bottom border.

On the bottom panel, you can execute this Python file by clicking on New Terminal and entering python handling_errors.py on the command line.
'''


def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to

    #       make sure no ZeroDivisionError occurs.
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as error:
        print("can't divide by zero no one is comming ?? {}".format(error))
    return(num_each, leftovers)


# The main code block is below; do not edit this
lets_party = 'y'
# or lets_party == 'Y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")


print('NEXT QUIZ')

try:
    new_number = int(input('enter the new number: '))
    divided_by = int(input('enter the new divided NUmber : '))
    calculations = new_number / divided_by
    print(calculations)
    # Exception can get you the error that happens really usefull love you kids:"D"
except Exception as e:
    print('Exception happens {}'.format(e))
