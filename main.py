'''def div2(num):
    num1=int(num[-1])
    l1=[0,2,4,6,8]
    if num1 in l1:
        return True
    else:
        return False
if __name__ == "__main__":
        number = (input('Enter a number: '));print(type(number))
        print(f"{number} is {'' if div2(number) else 'not'} divisible by 2")'''


###################################################################################################
'''def div3(num):
    for i in num:
        sum=0
        i=int(i)
        sum =sum+i
    if sum < 10:
        return div3
    else:
        if sum in [3,6,9]:
            return True
        else:
            return False
if __name__ == "__main__":
    number = (input('Enter a number: '));
    print(f"{number} is {'' if div3(number) else 'not'} divisible by 3")'''
###################################################################

'''def div5(num):
    num1=int(num[-1])
    num2=[0,5]
    if num1 in num2:
        return True
    else:
        return False
if __name__ == "__main__":
        number = (input('Enter a number: '));
        print(f"{number} is {'' if div5(number) else 'not'} divisible by 5")'''
############################################################################


'''def div9(num):
    sum=0
    for i in num:
        #num=int(i)
        sum = sum+int(i);print(sum);print(type(sum))
        if sum == 9:
            print(sum)
            return True
        elif sum > 9:
            return div9(str(sum))

if __name__ == "__main__":
    number = input('Enter a number: ')
    print(f"{number} is {'' if div9(number) else 'not'} divisible by 9")'''
    ###############################################################
'''def div3(num):
    for i in num:
        print(i)
        #i=int(i)
        sum=0
        sum =sum+int(i)
        print(sum)
        if sum > 9:
            return div3(sum)
        else:
            if sum in [3,6,9]:
                return True
            else:
                return False

if __name__ == "__main__":
    number = (input('Enter a number: '))
    print(f"{number} is {'' if div3(number) else 'not'} divisible by 3")'''


######################################################################################

'''def div4(num):
    num='0'+num
    if int(num[-2]) in[0,2,4,6,8] and int(num[-1]) in [0,4,8]:
        return True
    elif int(num[-2]) in [1,3,5,7,9] and int(num[-1]) in [2,6]:
        return True
    else:
        return False
if __name__ == "__main__":
    number = input('Enter a number: ')
    print(f"{number} is {'' if div4(number) else 'not'} divisible by 4")'''
#######################################################################
'''def div6(num):
    sum=0
    for i in str(num):
        sum=sum+int(i)
    print(sum)
    if sum > 9:
        return div6(sum)
    else:
        if sum in [3,6,9] and str(num[-1]) in [0,2,4,6,8]:
            return True
        else:
            return False
if __name__ == "__main__":
        number =int(input('Enter a number: '))
        print(f"{number} is {'' if div6(number) else 'not'} divisible by 6")'''
##########################################################################################################
'''def div6(num):
    sum=0
    for i in num:
        sum =sum+int(i)
    if sum > 9:
        k=str(sum)
        return div6(k)
    else:
        if sum in [3,6,9] and int(num[-1]) in [0,2,4,6,8]:
            return True
        else:
            return False
if __name__ == "__main__":
    number = (input('Enter a number: '))
    print(f"{number} is {'' if div6(number) else 'not'} divisible by 6")'''

########################################################################################################################
'''def div8(num):
    num='00'+num
    if int(num[-3]) in [0,2,4,6,8] and int(num[-2:]) in [8,16,24,32,40,48,56,64,72,80,88,96]:
        return True
    elif int(num[-3]) in [1,3,5,7]:
        sum=int(num[-2:])+4
        if sum in [8,16,24,32,40,48,56,64,72,80,88,96]:
            return True
    else:
        return False
if __name__ == "__main__":
    number = (input('Enter a number: '))
    print(f"{number} is {'' if div8(number) else 'not'} divisible by 8")'''
########################################################################################################
def div7(num):
    num1 = num[-1]; print(num1)
    n = 5*int(num1);print(n)
    num2=num[:-1];print(num2)
    n2=int(num[:-1])+n;print(n2)
    if n2 in [14,21,28,35,42,49,56,63,70,77,84,91,98]:
        return True
    else:
        return False
if __name__ == "__main__":
    number = (input('Enter a number: '))
    print(f"{number} is {'' if div7(number) else 'not'} divisible by 7")
#######################################################################################################################
