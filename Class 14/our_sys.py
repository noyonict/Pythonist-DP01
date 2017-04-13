lock = ['3', '5', '2']
print('A number lock has a 3 digit key')
user_key = input('CODE = ')
print(10*'*', 'HINT', 10*'*')
i = 0
correct_number = 0
f_placed = []
while i < 3:
    if lock[i] in lock:
        correct_number += 1
        if lock[i] == lock[i]:
            f_placed.append(True)
        else:
            f_placed.append(False)
    i += 1
print(correct_number)
if correct_number == 3:
    if f_placed[0] and f_placed[1] and f_placed[2]:
        print('All number is correct and well placed')
if correct_number == 2:
    if f_placed[0] and f_placed[1]:
        print('2 number is correct and well placed')
















