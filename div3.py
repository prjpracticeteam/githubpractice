def div3(n):
    sum = 0
    for i in n:
        sum = sum+int(i)
    if sum >= 10:
        return div3(n)
    else:
        if sum == 3 or sum == 6 or sum == 9:
            return True
        else:
            return False
if __name__ == "__main__":
    number = input('Enter a number:')
    print(f"{number} is {'' if div3(number) else 'not'} divisible by 3")
