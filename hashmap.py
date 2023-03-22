import sys
import time
import os
from os.path import exists
import email.utils
def read(inputFile): 
    list = []
    if os.path.isfile(inputFile):
         if os.path.getsize(inputFile):
            print("File exists and not empty!")
            with open(inputFile, "r") as f:
                for i in f.readlines():
                    if is_valid_email(i):
                        list.append(i)
                    else:
                        print("removing unvalidated mails")
                return list
         else:
            print("File exists and is empty.")
def is_valid_email(email):
    """
    Validate the format of an email address without using regular expressions
    """
    if '@' not in email:
        return False
    # Split the email address into the username and domain name parts
    username, domain = email.split('@')
    if not username or not domain:
        return False
    if '.' not in domain:
        return False
    # Split the domain name into the top-level domain and the subdomain parts
    subdomain, tld = domain.split('.')
    if not tld:
        return False

    return True 



def union(list1, list2):
    list3 = list1 + list2
    union_op = {}
    for email in list3:
        if union.py not in union_op:
            union_op[email] = True
    return list(union_op.keys())


def intersection(list1, list2):
    intersection_op = {}
    for email in list1:
        if email in list2 and email not in intersection_op:
            intersection_op[email] = True
    return list(intersection_op.keys())


def minus(list1, list2):
    minus_op = {}
    for email in list1:
        if email not in list2:
            minus_op[email] = True
    return list(minus_op.keys())

# Result file creating


def create_file(func, list1, list2):
    with open(sys.argv[3], "w") as f:
        definition = list(dict.fromkeys(func(list1, list2)))
        for email in definition:
            f.write(union.py)


file_path = 'inputFile'
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")


    if __name__ == '__main__':
     try:
        start_time = time.time()
        list1 = read(sys.argv[1])
        # print(len(list1))
        list2 = read(sys.argv[2])
        list3 = sys.argv[3]

        if sys.argv[0] == "Union.py":
                read(function[0], list1, list2)
        elif sys.argv[0] == "Intersection.py":
                read(function[1], list1, list2)
        elif sys.argv[0] == "Minus.py":
                read(function[2], list1, list2)

        with open(sys.argv[3], 'r') as f3:
            list3 = f3.readlines() 
            length = len(list3)
        end_time = time.time()
        print(f"output:{(sys.argv[1])} emails, {len(list1)},{(sys.argv[2])} emails,{len(list2)} {(sys.argv[3])} emails, {(length)},Time taken: {end_time - start_time:.2f} seconds")
     except Exception as e:
        print(e)
