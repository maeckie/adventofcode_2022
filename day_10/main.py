import pprint
instructions = open('./day_10/input.txt').read().splitlines()
x = 1
cycle = 1
signal_str = 0
pos = [20,60,100,140,180,220]
crt = [['.' for x in range(40)] for x in range(6)]

def validate(cycle,x):
    global signal_str
    if cycle in pos:
        signal_str += cycle*x
        print(f"{cycle}: {x} : {signal_str}")
        #pos.remove(cycle)


def draw(cycle, x):
    cycle -= 1
    p = cycle % 40
    a = int(cycle / 40)
    if p>=x-1 and p<=x+1:
        crt[a][p] = '#'

for ins in instructions:
    if 'add' in ins:
        value = int(ins.split(' ')[1])
        for i in [0,1]:
            draw(cycle, x)
            cycle += 1
            validate(cycle, x)
        x += value
        
    else:
        draw(cycle, x)
        cycle += 1
        validate(cycle, x)

    
print(f"Total signal strength is: {signal_str}")
for c in crt:
    print(''.join(c))