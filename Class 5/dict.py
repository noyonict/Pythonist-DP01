d = {}  # this is a dist not set
d = dict()
d['name'] = 'Noyon'
d['Name'] = 'Python'
d[1] = 'Number one'
print(d)
print(type(d))
d = dict(name = 'Noyon',
         phone = '01740399036',
         email = 'noyonmassive@gamil.com',
         location = 'DIU')
print(d)
d = {'name' : 'Noyon',
'phone' : '01740399036',
'email' : 'noyonmassive@gamil.com',
'location' : 'DIU'}
d[19] = 'Python calss no 5'
print(d)
print(d['name'])
print(d[19])
print(d.keys())
print(d.values())
#d.clear()
print(d.get('email')) # d['email']
print(d['email'])
print(d.items())
d1 = {'New Dict': 'New Value', 'New Email': 'New Email Value'}
d.update(d1)
print(d)
d['new Dict'] = {'n' : 'Name',
                 'E' : 'Email',
                 "phone" : '029394',
                 'list' : [1, 2, 44, 44, 5],
                 'set' : {1, 2, 3, 3 ,3, 3},
                 'tuple' : (1, 2, 2, 4, 2, 3)}
print(d)
print(d['new Dict']['E'], d['new Dict']['phone'])
print(d['new Dict']['list'][3])
print(d['new Dict']['tuple'].index(2))

for key, value in d.items():
    print(key, ' = ', value)
