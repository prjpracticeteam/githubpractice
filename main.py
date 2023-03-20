import sys
import time


def read(file):
    try:
        # file validation
        with open(file, 'r') as f:
            l = f.readlines()
            li = []
            for i in l:
                if i.strip():
                    li.append(i)
            if len(li) <= 0:
                raise Exception(f'{file} is exist but no data Found')
        # email validation    
            dic = {}
            for i in li:
                if '@' in i:
                    parts = i.split('@')
                    if len(parts) == 2 and '.' in parts[1]:
                        dic[i] = True
            return dic
    except FileNotFoundError:
        print(f'{file} is not Found')
        sys.exit(1)
    
        
def union(l1,l2):
    l3 = {}
    l3.update(l1)
    l3.update(l2)
    l4 = {}
    for i in l3:
        if i not in l4:
            l4[i] = True
    return l4

def intersec(l1,l2):
    l3 = {}
    for i in l1:
        if i in l2:
            l3[i] = True
    return l3

def minus(l1,l2):
    l3 = {}
    for i in l1:
        if i not in l2:
            l3[i] = True
    return  l3  

def write(file3, output):
    with open(file3, "w") as f3:
        f3.writelines(output)


if __name__ == "__main__":
    try:
        start_time= time.time()

        file1 = (sys.argv[1])
        file2 = (sys.argv[2])
        file3 = (sys.argv[3])

        l1 = read(file1)
        l2 = read(file2)
    
        if sys.argv[0] == 'union.py':
            output = union(l1,l2)
        elif sys.argv[0] == 'intersection.py':
            output = intersec(l1,l2)
        elif sys.argv[0] == 'minus.py':
            output = minus(l1,l2)
        else:
            raise Exception(f'Invalid Operation, valid operations are select union, intersection or minus')
        
        write(file3, output)
        
        end_time = time.time()
        print(f'Output: {sys.argv[1]} {sys.argv[2]} {sys.argv[3]} Time taken: {int(end_time - start_time)} sec')

    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)
