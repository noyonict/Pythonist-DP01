username = input('Username: ')
password = input('Password: ')
if len(password) >=6:
    print('Password is Strong')
else:
    print('Your password is not secured')



name = 'noyon'
password = '123noyon123'
name = input('Username: ')
password = input('Password: ')
if name == 'noyon' and password == '123noyon123':
    print('Log in')
else:
    print('Username or password incorrect')
'''

'''
name = ['nayon','mehedi','jibon']
print('mehedi' in name)
'''

username = ['nayon','jibon','mehedi']
password = ['123nayon123','jibon123','mehedi123']
n = input('Username: ')
p = input('Password: ')
if n in username and p in password:
    print('Log in')
else:
    print('Username or password incorrect')

i = username.index(n)
password[i]==p
