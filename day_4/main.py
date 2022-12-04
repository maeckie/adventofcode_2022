lines = list(map(lambda x: x.strip(),open('./day_4/input.txt').readlines()))
p1_overlaps = 0
p2_overlaps = 0
for areas in lines:
    elv_areas = list(map(lambda x: x.split('-'), areas.split(',')))
    if  (int(elv_areas[0][0]) >= int(elv_areas[1][0]) and int(elv_areas[0][1]) <= int(elv_areas[1][1]) or
        int(elv_areas[1][0]) >= int(elv_areas[0][0]) and int(elv_areas[1][1]) <= int(elv_areas[0][1]) 
        ):
        p1_overlaps += 1
    if (int(elv_areas[0][0]) <= int(elv_areas[1][1]) and int(elv_areas[0][1]) >= int(elv_areas[1][0]) or
        int(elv_areas[1][0]) <= int(elv_areas[0][1]) and int(elv_areas[1][1]) >= int(elv_areas[0][0])
        ):
        p2_overlaps += 1


print(f"Part1: {p1_overlaps}")
print(f"Part2: {p2_overlaps}")

