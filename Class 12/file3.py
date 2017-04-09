data = ''
try:
    with open('C:\\Users\\noyon\\Downloads\\178n.jpg', 'rb') as f:
        data = f.read()
except FileNotFoundError as v:
    print(v)
except Exception as e:
    print('No such file')

try:
    with open('C:\\Noyon\\copy.jpg', 'ab') as f:
        f.write(data)
except Exception as e:
    print('File not copy')


