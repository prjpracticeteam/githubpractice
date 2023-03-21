import sys
import time


def read(file):
    try:
        # file validation
        with open(file, 'r') as f:
            rl = f.readlines()
            li = []
            for i in rl:
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
    
        
def union(d1,d2):
    d3 = {}
    d3.update(d1)
    d3.update(d2)
    u = {}
    for i in d3:
        if i not in u:
            u[i] = True
    return u

def intersec(d1,d2):
    inter = {}
    for i in d1:
        if i in d2:
            inter[i] = True
    return inter

def minus(d1,d2):
    m = {}
    for i in d1:
        if i not in d2:
            m[i] = True
    return  m  

def write(file, output):
    with open(file, "w") as f:
        f.writelines(output)


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
