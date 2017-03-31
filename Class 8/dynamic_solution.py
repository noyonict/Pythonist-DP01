number = int(input('Enter number: '))
first_num= number
end_num = int(input('Enter last number: '))
a= int(input('Enter line number: '))
for i in range(1,a+1):
    for j in range(i):
        print(number,end=" ")
        if number==end_num:
            number=first_num
        else:
            number= number+1
    print()
