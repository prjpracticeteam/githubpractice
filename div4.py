
def isdiv4(number):

    tendigit = number[-2]
    onedigit = number[-1]

    if tendigit in ["0","2","4","6","8"] and onedigit in ["0","4","8"]:
        return True
    elif tendigit in ["1","3","5","7","9"] and onedigit in ["2","6"]:
        return True
    else:
        return False

if __name__ == "__main__":
    number = input("Enter a number:")
    print(f"{number} is {'' if isdiv4(number) else 'not'} divisble by 4")


