import os.path
import sys
import time
import argparse

def parse_args():

    parser = argparse.ArgumentParser(
        prog="unionprogram.py",
        description="This program will do union operation between two files which contains email address",
        usage='%(prog)s L1.txt L2.txt R.txt')
    parser.add_argument("L1.txt",  help="the first input file")
    parser.add_argument("L2.txt",  help="the second input file")
    parser.add_argument("R.txt",  help="the output file")
    return parser.parse_args()

''' function for the reading the file which contains email data and validating the email data 
with the validation function  and store into the dict '''
def readfiles(filename):
    read_map = {}
    if os.path.getsize(filename) == 0:
        raise Exception("file is empty")
    else:
        with open(filename, "r") as file:
            j = 0
            lines = file.readlines()
            for line in lines:
                email = line.strip()
                emails = emailvalidation(email)
                j += 1
                read_map[emails] = None

    return read_map, j

'''email validation function checking username,domain name not empty & not start with @,not end with.dot
& only one @ more then one .dot, domain_extension in rang of 2 to 6. 
'''
def emailvalidation(email):
    if '@' and '.' in email:
        username, domain_name = email.split("@")
        if len(username) > 0 and len(domain_name) > 0:
                #if email.index("@") > 0 and email.index('.') < len(email) - 1:
                #if email.count("@") == 1 and email.count('.') >= 1:
                # domain_extension = email.split('.')[-1]
                # if 2 <= len(domain_extension) <= 6:
            return email

''' union function which will do the union operations on the two dicts which are given as input
'''
def union(file1_dict, file2_dict):
    write_list = []
    for key in file1_dict:
        if key in file2_dict:
            write_list.append(key)
        if key in file2_dict:
            write_list.append(key)
    for key in file2_dict:
        if key not in file1_dict:
            write_list.append(key)

    return write_list

'''write function it will write data from write_file_data list  to output file'''
def writefile(write_file_name):
    with open(write_file_name, 'w') as file:
        for i in write_file_data:
            file.write(i + '\n')
    return write_file_name

# main
if __name__ == "__main__":
    start_time = time.time()
    try:

        args = parse_args()

        if len(sys.argv) != 4:
            raise Exception("sys argv are out of range")
        if not os.path.exists(sys.argv[1]) or os.path.getsize(sys.argv[1]) == 0:
            raise Exception(f"File '{args.sys.argv[1]}' "
                            f"{'does not exist' if not os.path.exists(sys.argv[1]) else 'is empty'}")
        if not os.path.exists(sys.argv[2]) or os.path.getsize(sys.argv[2]) == 0:
            raise Exception(f"File '{sys.argv[2]}' "
                            f"{'does not exist' if not os.path.exists(sys.argv[2]) else 'is empty'}")

        file1dict, j1 = readfiles(sys.argv[1])
        file2dict, j2 = readfiles(sys.argv[2])
        write_file_data = union(file1dict, file2dict)
        writefile(sys.argv[3])
        end_time = time.time()

        ''' it will print the files and files data length and time taken to process'''
        print(
            f"{sys.argv[1]}: {j1} emails, {sys.argv[2]} :{j2} emails,{sys.argv[3]}:{len(write_file_data)}:"
            f" time_taken {int(end_time - start_time)}")
        sys.exit(0)

    except Exception as e1:

        print("error:{}".format(str(e1)))
        sys.exit(1)
