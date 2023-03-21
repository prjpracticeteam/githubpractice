
import time
import sys
import os

def read_file(file_path):
    """
    if the given file is not empty, it should raed the emails in files one by one
    """
    try:
        phani = []
        if os.path.isfile(file_path):
            if os.path.getsize(file_path):
                print("File exists and not empty!")
                print(read_file.__doc__)
                with open(file_path, "r") as f:
                    for i in f.readlines():
                        if validate_email(i):
                            phani.append(i)
                        else:
                            print("removing unvalidated mails")
                            print(validate_email.__doc__)
                    return phani
            else:
                print("File exists and is empty.")
    except Exception as e:
        print(e)
        sys.exit(1)


def validate_email(email):
    '''
    if the emails in Files are not matching the validation rules, it will automatically remove unvalidated emails
    '''
    try:
        # Check if email has only one "@" character
        if email.count("@") != 1:
            return False

        # Split the email into local and domain parts
        local, domain = email.split("@")

        # Check if local and domain parts are not empty
        if not local or not domain:
            return False

        # Check if domain has at least one "." character
        if "." not in domain:
            return False

        return True
    except Exception as e:
        print(e)
        sys.exit(1)


def union(list1, list2):
    list3 = []
    for item in list1:
        if item not in list3:
            list3.append(item)
    for item in list2:
        if item not in list3:
            list3.append(item)
    return list3


def intersection(list1, list2):
    list3 = []
    for item in list1:
        if item in list2:
            list3.append(item)
    return list3


def minus(list1, list2):
    list3 = []
    for item in list1:
        if item not in list2:
            list3.append(item)
    return list3


def write_file(list3):
    with open(sys.argv[3], 'w') as r:
        for i in list3:
            r.write(i)
    with open(sys.argv[3], 'r') as r:
        h = r.readlines()
        return h

def main():
    try:
        if len(sys.argv) == 4:
            print("Usage: python script.py arg1 arg2...")
        else:
            print("list index out of range")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
        start_time = time.time()
        list1 = read_file(sys.argv[1])
        list2 = read_file(sys.argv[2])

        l1 = union(list1, list2)
        l2 = intersection(list1, list2)
        l3 = minus(list1, list2)

        final1 = write_file(l1)
        final2 = write_file(l2)
        final3 = write_file(l3)

        end_time = time.time()
        print(f"Output: {sys.argv[1]}: {len(list1)} emails, {sys.argv[2]}: {len(list2)} emails, {sys.argv[3]}: {len(final1)} emails, Time taken: {int(end_time - start_time)} seconds.")
        print(f"Output: {sys.argv[1]}: {len(list1)} emails, {sys.argv[2]}: {len(list2)} emails, {sys.argv[3]}: {len(final2)} emails, Time taken: {int(end_time - start_time)} seconds.")
        print(f"Output: {sys.argv[1]}: {len(list1)} emails, {sys.argv[2]}: {len(list2)} emails, {sys.argv[3]}: {len(final3)} emails, Time taken: {int(end_time - start_time)} seconds.")
    except Exception as e:
        print(e)