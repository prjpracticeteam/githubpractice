import sys
import time
import os.path
import argparse
def read(inputFile):
    list = []
    with open(inputFile,'r') as f :
        for email in f.readlines():
            if email not in list:
                list.append(email) 
    return list  
 # union      
def union(list1, list2):
   union = [] 
   for email in list1:
     if email   in union:
        union.append(email)
     for email in list2:
        if email not in list2:
            union.append(email)
   return union
def intersection(list1, list2):
    intersection = []
    for email  in list1:
        if email in list2: 
            intersection.append(email)
    return intersection 
# Minus
def minus(list1,list2):
    minus = []
    for email in list1:
        if email not in minus:
            minus.append(email)
    for email in list2:
        if email not in minus:
            minus.append(email)
    return minus

#Result file creating
def create_file( func,list1,list2):
    with open(sys.argv[3], "w") as file3:
        definition = list(dict.fromkeys(func,(list1,list2))) 
        for email in definition:
            file3.write(email)
#File validation
# file_path ="testing_p3" 
# if os.path.exists(file_path):
#     print("File exists")
# else:
#     print("File does not exist")
file_path = 'project3\L1.txt'

# Check if the file exists
if os.path.exists(file_path):
    # Check if the file is not empty
    if os.path.getsize(file_path) > 0:
        print(f'The file "{file_path}" exists and is not empty.')
    else:
        print(f'The file "{file_path}" exists but is empty.')
else:
    print(f'The file "{file_path}" does not exist.')  
               
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
             


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = argparse.ArgumentParser(description='two input files containing email addresses.')
        parser.add_argument('File1', help='First input file')
        parser.add_argument('File2', help='Second input file')
        parser.add_argument('output', help='Output file')
        args = parser.parse_args()
        list1 = read(args.File1)
         #print(len(list1))
        list2 = read(args.File2)
        create_file(args.File1,args.File2)


        is_valid_email(list1)
        print(is_valid_email)
        is_valid_email(list2)
        print(is_valid_email)
         # definition = create_file(sys.argv[3])
         #print(len(list2))  
        with open(sys.argv[3], 'r') as f:
         list3 = f.readlines()
         length =len(list3)
        if sys.argv[0] == "Union.py":
            read(function[0], list1, list2)
        elif sys.argv[0] == "Intersection.py":
            read(function[1], list1, list2)
        elif sys.argv[0] == "Minus.py":
            read(function[2], list1, list2)
        end_time = time.time()
         # print(f"{(sys.argv[1])} emails,{(union)}, {(sys.argv[2])} emails, {len(sys.argv[1])},Time taken: {end_time - start_time:.2f} seconds")
        print(f"output:{(sys.argv[1])} emails,{len(list1)},{(sys.argv[2])} emails, {(len(list2))},{(sys.argv[3])} emails,{(length)}, Time taken: {end_time -start_time} seconds")
    except Exception as e:
        print(e)   