game_order = open('./day_2/input.txt').readlines()
points = {'X': 1, 'Y': 2, 'Z': 3}
action_map = {'A': 'X', 'B': 'Y', 'C': 'Z'}

p2_action_map = {'A': [3,4,8], 'B': [1,5,9], 'C':[2,6,7]}    




def eval_game(a,b):
    if a == b:
        return 3 + points[b] 
    if a == 'X' and b == 'Y':
        return 6 + points[b] 
    elif a == 'X':
        return points[b] 
    if a == 'Y' and b == 'Z':
        return 6 + points[b] 
    elif a == 'Y':
        return points[b] 
    if a == 'Z' and b == 'X':
        return 6 + points[b] 
    elif a == 'Z':
        return points[b] 
        
def part1():
    total_points = 0   
    for game in game_order:
        g = game.strip().split(' ')
        total_points += eval_game(action_map[g[0]], g[1])

    print(f"Part 1 total score is: {total_points}")


def part2():
    total_points = 0
    for game in game_order:
        g = game.strip().split(' ')
        if g[1] == 'X':
            total_points += p2_action_map[g[0]][0]
        elif g[1] == 'Y':
            total_points += p2_action_map[g[0]][1]
        elif g[1] == 'Z':
            total_points += p2_action_map[g[0]][2]
    print(f"Part 2 total score is: {total_points}")


part1()
part2()