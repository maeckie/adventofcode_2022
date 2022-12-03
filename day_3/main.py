import string

score = 0
def part1():
    with open('./day_3/input.txt') as data:
        for rucksack in data.readlines():
            rucksack = rucksack.strip()
            l = len(rucksack)
            a = list(set(rucksack[0:int(l/2)]) & set(rucksack[int(l/2):]))[0]
            pos = string.ascii_lowercase.index(a.lower())
            score += pos+27 if a.isupper() else  pos+1
    print(f"Part 1 score: {score}")    

def part2():
    rucksacks = list(map(lambda x: x.strip(), open(('./day_3/input.txt')).readlines()))
    i = 0
    score = 0
    while i+2 < len(rucksacks):
        a = list(set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]))[0]
        pos = string.ascii_lowercase.index(a.lower())
        score += pos+27 if a.isupper() else  pos+1
        i+=3
    print(f"Part 2 score: {score}")    
    



part2()
