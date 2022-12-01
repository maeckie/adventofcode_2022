import numpy as np

all = []
with open('input.txt') as f:
    lines = f.read().splitlines()
    a = []
    for l in lines:
        if l == '':
            all.append(a)
            a = []
        else:
            a.append(int(l))
    all.append(a)

def part_1():
    print(max(list(map(lambda x: sum(x), all))))

def part_2():
    q=list(map(lambda x: sum(x), all))
    q.sort(reverse=True)
    print(sum(q[0:3]))

     
part_1()
part_2()    

    
