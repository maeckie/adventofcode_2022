lines = list(map(lambda x: x.strip(),open('./day_4/input.txt').readlines()))
p1_overlaps = 0
p2_overlaps = 0
for areas in lines:
    elv_areas = list(map(lambda x: x.split('-'), areas.split(',')))
    left = range(int(elv_areas[0][0]), int(elv_areas[0][1])+1)
    right = range(int(elv_areas[1][0]), int(elv_areas[1][1])+1)
    if all(elem in left  for elem in right) or all(elem in right  for elem in left):
        p1_overlaps += 1

    if any(elem in left  for elem in right):
        p2_overlaps += 1        

print(f"Part1: {p1_overlaps}")
print(f"Part2: {p2_overlaps}")

