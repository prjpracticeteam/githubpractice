# def div7(number):
#     number = str(number)
#     last = number[-1]
#     rest = number[0:-1]
#
#     a = (int(last) * 5) + int(rest)
#
#     if a in [7,49]:
#         return True
#     elif a > 7:
#         return div7(a)
#     else:
#         return False
#
#
# if __name__ == "__main__":
#     number = input("Enter a number:")
#     print(f"{number} is {'' if div7(number) else 'not'} divisble by 7")

#######################################################################################################

def div7(number):

    last = number[-1]
    rest = number[0:-1]

    a = int(last) * 5 + int(rest)
    print(type(a))

    if a in [7,49]:
        return True
    elif a > 7:
        return div7(str(a))
    else:
        return False

if __name__ == "__main__":
    number = input("Enter a number:")
    print(f"{number} is {'' if div7(number) else 'not'} divisble by 7")
