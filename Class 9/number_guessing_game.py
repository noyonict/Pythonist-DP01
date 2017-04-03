import random

def chances(num):
    print('You have', 5 - (num + 1), 'chances left.')

result = True
def number_guessing_game(lb='First', end_range=50, guessing_num=37, chance=5):
    global result
    print(lb)
    print('Can you guesses my number. My number between 0 to',  end_range)
    print('You have 5 chances.')
    num = guessing_num

    for i in range(chance):
        user_input = int(input('Enter your number: '))
        if num < user_input:
            print('Your number is bigger then my number.')
            chances(i)
        elif num > user_input:
            print('Your number is less then my number.')
            chances(i)
        else:
            print('You win!')
            result = False
            next_l = input('Do you want to play next? y/n')
            if next_l == 'n':
                print('Thank you!')
            else:
                number_guessing_game(lb='Second', guessing_num=29, end_range=60)
            break
    if result:
        print('You Failed!')
        print('Please try again!')
        number_guessing_game()

my_number = random.randint(0, 50)
#print(my_number)
number_guessing_game(guessing_num = my_number)
