lines = open('./day_5/input_test.txt').readlines()

stacks = {}
for line in lines:
    if '[' in line:
        i = 0
        while i < len(line):
            if str(line[i]).isalpha():
                c = int((i+1)/3)
                if c == 0:
                    c = 1
                if c not in stacks:
                    stacks[c] = []
                stacks[c].insert(0,line[i])
            i+=1

print(stacks)

