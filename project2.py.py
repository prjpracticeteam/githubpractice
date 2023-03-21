# Take input from user
numbers = input("Enter comma-separated numbers: ")

# Split the input string into a list of numbers
numbers_list = numbers.split(",")

# Loop through each number in the list and check its divisibility
for num in numbers_list:
    num = int(num.strip())  # convert string to integer and remove whitespace
    divisors = []  # initialize list to store the divisors of the current number

    # Check divisibility by 2, 4, and 5
    a = str(num)
    b = int(a[-1])
    if b == 8 or b == 6 or b == 4 or b == 2 or b == 0:
        divisors.append(2)
    if b == 8 or b == 4 or b == 0:
        divisors.append(4)
    if b == 5 or b == 0:
        divisors.append(5)

    # Check divisibility by 3 and 9
    sum=0
    for i in str(num):
     sum = sum + int(i)
    if (sum == 3 or sum == 6 or sum == 9):
        divisors.append(3)
    if (sum == 9 or sum ==0):
        divisors.append(9)

    # Print the result for the current number
    if len(divisors) > 0:
        print(f"{num}: is divisible by {', '.join(map(str, divisors))}")
    else:
        print(f"{num}: is not divisible")
