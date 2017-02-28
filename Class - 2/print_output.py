a = 7
b = 3
sum = a + b
print(sum)  # 10
#print(a + ' + ' + b + ' = ' + sum)  # error
print(str(a) + ' + ' + str(b) + ' = ' + str(sum))  # 7 + 3 = 10
print(a, '+', b, '=', sum)  # 7 + 3 = 10
print('{} + {} = {}'.format(a, b, sum))  # 7 + 3 = 10

# input from user
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
sum = a + b
print(a, '+', b, '=', sum)  # a + b = sum
print('{} + {} = {}'.format(a, b, sum))  # a + b = sum

'''
we learn today
1. Variable declaration, how its works?
2. Data type (int, float, str, bool) & Type cast
3. How to show different variable in print function ex: print(a, '+', b, '=', sum)
4. User input. ex: input('Enter something')
'''


