def div5(number):

    a = int(number[-1])

    if a in [0,5]:
        return True
    else:
        return False

if __name__ == "__main__":
    number = input("Enter a number:")
    print(f"{number} is {'' if div5(number) else 'not'} divisble by 5")
