def is_prime(number):
    if number == 2:
        return True
    elif number == 4 or number <= 1:
        return False
    for i in range(3, round(number/2)+1, 2):
        if number % i == 0:
            return False
    return True
user_input = int(input('Enter a number: '))
while True:
    if is_prime(user_input):
        print('{} is a prime number'.format(user_input))
    else:
        print('{} is not a prime number.'.format(user_input))
    c = input('Do you want to do it again?(y/n)-> ')
    if c == 'n':
        break
    else:
        user_input = int(input('Enter a number: '))












