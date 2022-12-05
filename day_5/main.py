import re
lines = open('./day_5/input.txt').readlines()
test = {1: ['Z','N'],
        2: ['M','C','D'],
        3: ['P']
}

real = {1: ['W','M','L','F'],
        2: ['B','Z','V','M','F'],
        3: ['H','V','R','S','L','O'],
        4: ['F','S','V','Q','P','M','T','J'],
        5: ['L','S','W'],
        6: ['F','V','P','M','R','J','W'],
        7: ['J','Q','C','P','N','R','F'],
        8: ['V','H','P','S','Z','W','R','B'],
        9: ['B','M','J','C','G','H','Z','W']
        }
stacks = real

def part1():
    for line in lines:
        if 'move' in line:
            m = re.search('move (\d+) from (\d+) to (\d+)', line)
            amount = int(m.group(1)) 
            start = int(m.group(2)) 
            end = int(m.group(3)) 
            for i in range(amount):
                a = stacks[start].pop()
                stacks[end].append(a)

def part2():
    for line in lines:
        if 'move' in line:
            m = re.search('move (\d+) from (\d+) to (\d+)', line)
            amount = int(m.group(1)) 
            start = int(m.group(2)) 
            end = int(m.group(3))
            stacks[end].extend(stacks[start][-amount:])
            stacks[start] = stacks[start][:-amount]



part2()
result = ''
for stack in stacks.values():
    result += stack.pop()
print(result)
    
    