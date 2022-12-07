import pprint
terminal = open('./day_7/input.txt').read().splitlines() 

filesystem = {}
where = []
for line in terminal:
    if line.startswith('$'):
        cmd = line.split(' ')
        if cmd[1] == 'cd':
            directory = cmd[2]
            if directory == '..':
                where.pop()
            else:
                where.append(directory)
    else:
        
        w = ''.join(where)
        if w not in filesystem:
            filesystem[w] = 0 
        
        size = line.split(' ')[0]
        if size.isnumeric():
            filesystem[w] += int(size)

free = 70000000 - sum(filesystem.values())
needed = 30000000 - free

tot = 0 
larger = []
for folder in filesystem:
    s = 0 
    for f2 in filesystem:
        if str(folder) in str(f2):
            s += filesystem[f2]
    if s <=100000:
        tot+= s
    if s >= needed:
        larger.append(s)

print(f"Total size: {tot}")
print(f"Smallest size to be deleted: {min(larger)}")



                

             
            
        