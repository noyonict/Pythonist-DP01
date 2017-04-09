import os
import time
print(os.getcwd())
os.mkdir('new noyon')
time.sleep(1)
os.mkdir('new noyon1')
time.sleep(5)
os.rmdir('new noyon')
time.sleep(5)
os.rmdir('new noyon1')
print(os.getcwd())


