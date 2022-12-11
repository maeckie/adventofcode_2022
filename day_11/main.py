
import operator
ops = { "+": operator.add, "-": operator.sub, '*': operator.mul, '%': operator.floordiv }


class Monkey:
    items = []
    operation = ''
    operation_amount = 0
    test = 0
    true = 0
    false = 0
    inspected_items = 0
    def __init__(self):
        None

def print_monkey(monkey):
    print(f"items: {monkey.items}")
    print(f"operation: {monkey.operation}")
    print(f"operation_amount: {monkey.operation_amount}")
    print(f"test: {monkey.test}")
    print(f"true: {monkey.true}")
    print(f"false: {monkey.false}")
    print("-----")

def calc_worry(val, op, op_amount):
    if op_amount == 'old':
        return ops[op](val,val)
    return ops[op](val,int(op_amount))

    

monkey = None
monkies = []


for line in open('./day_11/input.txt').read().splitlines():
    if line.startswith('Monkey'):
        monkey = Monkey()
    elif 'Starting' in line:
        
        l = line.split(':')[1].split(',')
        l = list(map(lambda x: x.strip(), l))
        monkey.items = list(map(lambda y: int(y), l))
        
    elif 'Operation' in line:
        l = line.split(' ')
        monkey.operation = l[-2]
        monkey.operation_amount = l[-1]
    elif 'Test' in line:
        monkey.test = int(line.split(' ')[-1])
    elif 'true' in line:
        monkey.true = int(line.split(' ')[-1])
    elif 'false' in line:
        monkey.false = int(line.split(' ')[-1])
    else:
        monkies.append(monkey)
monkies.append(monkey)

mod = 1
for m in monkies:
    mod *= m.test

for i in range(10000):
    for monkey in monkies:
        for item in monkey.items:
            monkey.inspected_items += 1
            #worry_level = int(calc_worry(item, monkey.operation, monkey.operation_amount)/3)
            worry_level = calc_worry(item, monkey.operation, monkey.operation_amount) % mod
            if worry_level % monkey.test == 0:
                monkies[monkey.true].items.append(worry_level)
            else:   
                monkies[monkey.false].items.append(worry_level)
        monkey.items = []

monkey_business = sorted([x.inspected_items for x in monkies], reverse=True)
#for m in monkies:
#    print(m.inspected_items)
print(monkey_business[0]*monkey_business[1])
    
            

            
            
