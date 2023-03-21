
def isdiv3(number):

    s = str(number)
    sum =0
    for i in s:
        sum = sum + int(i)
        print(sum)

    if sum in [3,6,9]:
        return True
    elif sum >9:
        return isdiv3(sum)
    else:
        return False

if __name__ == "__main__":
    number = input("Enter a number:")
    print(f"{number} is {'' if isdiv3(number) else 'not'} divisble by 3")

