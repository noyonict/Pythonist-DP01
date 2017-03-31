number = int(input('Enter number: '))
a= int(input('Enter line number: '))
for i in range(1,a+1):
    for j in range(i):
        print(number,end=" ")
        number = number + 1
        if number==6:
            number=1
    print()

