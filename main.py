import sys
import time


def read(file):
    with open (file, 'r') as f:
        l = f.readlines()
    return l


def union(l1, l2):
    u = []
    for i in l1:
        u.append(i)
    for i in l2:
        if i not in u:
            u.append(i)
    return u


def intersection(l1,l2):
    u = []
    for i in l1:
        if i in l2:
            u.append(i)
    return u


def minus(l1,l2):
    u = []
    for i in l1:
        if i not in l2:
            u.append(i)
        return u



def write(file, result):
    with open(file, 'w') as f:
        f.write(''.join(result))


if __name__ == '__main__':
    start_time = time.time()
    l1 = read(sys.argv[1])
    l2 = read(sys.argv[2])
    union.py = union(l1, l2)
    inter.py = intersection(l1, l2)
    minus.py=minus(l1,l2)
    write(sys.argv[3], res)
    end_time = time.time()
    print(f"{end_time-start_time} seconds")
