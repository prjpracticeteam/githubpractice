# def div6(number):
#
#     a = str(number)
#     sum = 0
#
#     for i in a:
#         sum = sum + int(i)
#         print(sum)
#
#     if int(a[-1]) in [0,2,4,6,8] and sum in [3,6,9]:
#         return True
#     elif sum > 9:
#         return div6(sum)
#     else:
#         return False
#
# if __name__ == "__main__":
#     number = input("Enter a number:")
#     print(f"{number} is {'' if div6(number) else 'not'} divisble by 6")

###################################################################################################
def div6(number):

    a = str(number)
    sum =0

    for i in a:
        sum = sum + int(i)
        print(sum)

    if int(a[-1]) in [0,2,4,6,8] and sum in [3,6,9]:
        return True
    elif sum >9:
        return div6(sum)
    else:
        return False


if __name__ == "__main__":
    number = input("Enter a number:")
    print(f"{number} is {'' if div6(number) else 'not'} divisble by 6")





