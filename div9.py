def div9(number):

    sum = 0

    for i in number:
        sum = sum + int(i)

    if sum in [9]:
        return True
    elif sum >9:
        return div9(str(sum))
    else:
        return False

if __name__ == "__main__":
    number = input("Enter a number:")
    print(f"{number} is {'' if div9(number) else 'not'} divisble by 9")







