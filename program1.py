number = input("enter the numbers ")
b = number.split(',')
print(b)
for i in b:
    print(i)
    # print(type(i))
    if int(i) % 2 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")