def div8(number):

    last = number[-1]
    rest = number[0:-1]

    a = int(rest) * 2 + int(last)
    print(type(a))

    if a in [8]:
        return True
    elif a > 8:
        return div8(str(a))
    else:
        return False

if __name__ == "__main__":
    number = input("Enter a number:")
    print(f"{number} is {'' if div8(number) else 'not'} divisible by 8")










